# Team

## Thông tin nhóm

- Tên nhóm: `Nhom123`
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Nhom123-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Võ Hồng Lương| 2A202603839 | Vận hành và pháp lý | Đúng |
|   2 | Hồ Anh Tú | 2A202603811 | Kỹ sư cổng| _|
|   3 | Lê Đức Trúc Lâm | 2A202603787 | Kỹ sư cổng | _ |
|   4 | Triệu Hải Đăng Trình | 2A202603874 | Sản phẩm và kinh doanh | _ |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## VoHongLuong-2A202603839

### Phần việc phụ trách

Vai Vận hành và pháp lý, kiêm trưởng nhóm và chủ repo. Câu 1.2, 1.4 (Phiếu A mục A1, A2); ký tiêu chí trên `main` (Phiếu A mục A5); câu 2.4 HAZOP vòng 1 và checklist 9 nhóm việc (Phiếu B mục B4, B5); câu 2.10 (`config/operating_gates.json` mục `operations`, `legal`; Phiếu B mục B7.5 runbook 1–3, B7.6 giờ cao điểm). Vòng 2: phần riêng thẻ S7 (C3.3), HAZOP của thẻ (C4), câu 3.3, risk register (C10), runbook 4–5 (C11), gom bài nộp (`submission/`).

### Đóng góp cụ thể

- Tạo repo, mời thành viên, điền bảng thành viên và thông tin nhóm.
- Câu 1.2: mục tiêu của chị Oanh (sổ hoàn tiền và lỗi hãng khớp với hãng, shop mà không sửa tay) và chị Hạnh (ca chuyển sang vừa sức 6 ca/giờ, SLA 60 phút, có ghi chú giải thích).
- Câu 1.4: telemetry production đo lỗi ghi oan cho mỗi hãng trong 24 giờ, đối chiếu `delay_cause` với `fault_causes`, ngưỡng đỏ 1 lỗi oan.
- HAZOP vòng 1 trên `file_carrier_fault` (5 dòng kỹ thuật, 3 dòng ngoài kỹ thuật) rút từ `lab10/agent.py`; checklist 9 nhóm việc có PIC từng dòng.
- Câu 2.10: PIC NV-TUNG, người duyệt NV-HANH, 1 người trực, 6 ca/giờ, chờ tối đa 60 phút, 4 điều kiện dừng, `decision_note` bật, kiểm mẫu 10%, chặn `customer_note` và `recipient_contact` khi gửi hãng, bắt buộc có nguyên nhân trễ trước khi ghi lỗi hãng; runbook 1–3 và giờ cao điểm khớp tiêu chí đã ký.
- Soát và gộp bài: khôi phục câu 1.4 bị ghi đè ở nhánh `trinh`, sửa câu 1.3, phát hiện lỗi message và kiểu xuống dòng ở lần ký đầu rồi chuyển tiêu chí sang `main` và ký lại trước lần đánh giá đầu tiên.

### Bằng chứng

Commit `ce077b4` (câu 1.4), `a3f99aa` (câu 1.2), `fee7aea` (khôi phục Phiếu A), `02bfbf5` (sửa câu 1.3), `0c5a8a5` và `649385a` (đưa tiêu chí sang `main`, ký), `4e53b41` (HAZOP, checklist, câu 2.10, runbook). Mã lần chạy: bổ sung sau khi bàn chạy đánh giá.

Có dùng trợ lý AI (Claude Code) để đọc code của lab, viết nháp câu 1.2, 1.4, HAZOP, checklist, runbook và soát các nhánh trước khi merge; mọi con số và quyết định đã được đối chiếu với `data/world.json` và `lab10/` và do tôi chốt.

### Exit ticket

(Viết sau buổi học.)

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
