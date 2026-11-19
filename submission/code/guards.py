"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def _facts(ctx, order_id):
    """Nguồn sự thật cho một đơn: kiện ticket nói tới (hoặc kiện trễ nhất), độ trễ theo tracking DB,
    bản chính sách đang hiệu lực theo ngày (không theo cờ index_active)."""
    order = ctx.tools.lookup_order(order_id)
    if order is None or not order.get("parcels"):
        return None
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is None:
        return None
    return order, parcel, policy, H.db_delay_days(parcel, ctx.as_of)


def pre_guard(ctx):
    # CỔNG 1 (HAZOP B4 dòng INVALID; drift B3 REFUND-v3 -> REFUND-v4 ngày 01/12/2026):
    # ghim bản chính sách theo ngày hiệu lực, không tin cờ index_active có thể cập nhật trễ.
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is not None:
        return Verdict.allow(policy_id=policy["policy_id"])
    return Verdict.allow()


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")

    # CỔNG 2 (pre-mortem B6 lý do kỹ thuật; HAZOP B4 dòng PERTURBED, INCAPABLE; B2 lỗi 1 của T-002@55):
    # tiền hoàn không bao giờ vượt quyền lợi tính từ tracking DB, bất kể số ngày khách tự khai.
    if tool == "issue_refund":
        if action.get("basis") == "fail_open":
            return Verdict.escalate("LLM lỗi, agent tự hoàn kiểu fail_open: chuyển người duyệt")
        if action.get("payer", "LOGIX") != "LOGIX":
            return Verdict.escalate("bên chịu tiền bị đổi theo chữ trong ticket hoặc ghi chú: chuyển người duyệt")
        facts = _facts(ctx, action.get("order_id"))
        if facts is None:
            return Verdict.escalate("không đối chiếu được đơn với tracking DB: chuyển người duyệt")
        order, parcel, policy, delay = facts
        entitled = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
        asked = int(action.get("amount_vnd") or 0)
        if asked > entitled:
            ctx.log("refund_vs_db", asked=asked, entitled=entitled, db_delay_days=delay,
                    policy_id=policy["policy_id"])
            if entitled <= 0:
                return Verdict.deny(f"theo tracking DB trễ {delay} ngày, chưa đủ điều kiện hoàn")
            return Verdict.modify(f"hạ về quyền lợi theo tracking DB ({delay} ngày)", amount_vnd=entitled)

    # CỔNG 3 (HAZOP B4 dòng WRONG, INCOMPLETE, PERTURBED; B2 lỗi 2 của T-002@55; câu 1.3, 1.4):
    # chỉ ghi lỗi cho hãng khi chính sách đang hiệu lực coi kiện trễ thật sự là lỗi hãng,
    # và ghi đúng kiện, đúng hãng, đúng số ngày theo tracking DB.
    if tool == "file_carrier_fault":
        facts = _facts(ctx, action.get("order_id"))
        if facts is None:
            return Verdict.deny("không đối chiếu được đơn với tracking DB: không ghi lỗi hãng")
        order, parcel, policy, delay = facts
        if not H.carrier_at_fault(policy, parcel, delay):
            ctx.log("fault_vs_db", parcel_id=parcel["parcel_id"], db_delay_days=delay,
                    delay_cause=parcel.get("delay_cause"), policy_id=policy["policy_id"])
            return Verdict.deny(f"tracking DB: trễ {delay} ngày, nguyên nhân {parcel.get('delay_cause')}, "
                                "không phải lỗi hãng theo chính sách")
        want = {"parcel_id": parcel["parcel_id"], "carrier_id": parcel["carrier_id"],
                "driver_id": parcel.get("driver_id"), "delay_days": delay}
        if any(action.get(k) != v for k, v in want.items()):
            return Verdict.modify("ghi lỗi theo đúng kiện trễ và số ngày của tracking DB", **want)

    # CỔNG 4 (vòng 2, thẻ S7; Phiếu C C5 câu 3.2, C6 nhánh [1] [2] [3], C10 dòng 1):
    # danh sách CHO PHÉP thay cho danh sách chặn. Thông báo gửi hãng là dữ liệu rời khỏi LogiX tới bên thứ ba,
    # nên chỉ giữ các khoá mà chính sách đang hiệu lực liệt kê trong carrier_notice_fields; mọi khoá khác bị bỏ,
    # dù tên là gì. Giá trị district lấy lại từ đơn trong DB để trường được phép không chở chữ khách gõ.
    # Dùng modify (bỏ khoá thừa rồi vẫn gửi), không escalate, để không đẩy ca hợp lệ sang người duyệt (C10 dòng 2).
    if tool == "notify_carrier":
        policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
        allowed = list((policy or {}).get("carrier_notice_fields") or [])
        if not allowed:
            return Verdict.deny("không xác định được danh sách trường được phép gửi hãng: không gửi")
        payload = action.get("payload") or {}
        clean = {k: payload[k] for k in allowed if k in payload}
        order = ctx.tools.lookup_order(action.get("order_id") or payload.get("order_id"))
        if order is not None and "district" in allowed:
            clean["district"] = (order.get("recipient") or {}).get("district")
        if clean != payload:
            ctx.log("carrier_notice_allowlist", dropped=sorted(set(payload) - set(allowed)),
                    allowed=allowed, policy_id=(policy or {}).get("policy_id"))
            return Verdict.modify("chỉ gửi hãng các trường trong carrier_notice_fields của chính sách đang hiệu lực",
                                  payload=clean)

    return Verdict.allow()
