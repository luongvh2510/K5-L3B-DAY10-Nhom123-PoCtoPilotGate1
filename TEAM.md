# Team

## Thông tin nhóm

- Tên nhóm: `Nhom123`
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Nhom123-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S7

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

Vai Vận hành và pháp lý, kiêm trưởng nhóm và chủ repo. Vòng 1: câu 1.2, 1.4 (Phiếu A mục A1, A2); ký tiêu chí trên `main` (A5); câu 2.4 HAZOP vòng 1 và checklist 9 nhóm việc (Phiếu B mục B4, B5); câu 2.10 (`config/operating_gates.json` mục `operations`, `legal`; B7.5 runbook 1–3, B7.6 giờ cao điểm). Hỗ trợ thêm: câu 2.8 (B7.3), quyết định v1 (B8). Vòng 2 (thẻ S7): C1, phần riêng của thẻ C3.3, HAZOP của thẻ C4, câu 3.3 (C5), C7 phần `legal` và `operations`, risk register (C10), runbook 4–5 (C11), gom bài nộp (`submission/`).

### Đóng góp cụ thể

Vòng 1
- Tạo repo, mời thành viên, điền bảng thành viên và thông tin nhóm; soát và gộp mọi nhánh của bàn.
- Câu 1.2: mục tiêu của chị Oanh (sổ hoàn tiền và lỗi hãng khớp với hãng, shop mà không sửa tay) và chị Hạnh (ca chuyển sang vừa sức 6 ca/giờ, SLA 60 phút, có ghi chú giải thích).
- Câu 1.4: telemetry production đo lỗi ghi oan cho mỗi hãng trong 24 giờ, đối chiếu `delay_cause` với `fault_causes`, ngưỡng đỏ 1 lỗi oan.
- Ký tiêu chí: phát hiện lần ký đầu sai message commit và hash lệch do xuống dòng CRLF trên Windows; thêm `.gitattributes` (LF), chuyển tiêu chí sang `main` và ký lại trước lần đánh giá đầu tiên.
- HAZOP vòng 1 trên `file_carrier_fault` (5 dòng kỹ thuật, 3 dòng ngoài kỹ thuật) rút từ `lab10/agent.py`; checklist 9 nhóm việc có PIC từng dòng.
- Câu 2.10: PIC NV-TUNG, người duyệt NV-HANH, 1 người trực, 6 ca/giờ, chờ tối đa 60 phút, 4 điều kiện dừng, `decision_note` bật, kiểm mẫu 10%, chặn `customer_note` và `recipient_contact` khi gửi hãng, bắt buộc có nguyên nhân trễ trước khi ghi lỗi hãng; runbook 1–3 và giờ cao điểm khớp tiêu chí đã ký.
- Câu 2.8: behavioral test số ngày trễ khách khai, hai ticket hiểm O-1004 và O-1024 kèm kết quả trace.
- Quyết định v1 **Tiếp tục**: mốc prepared đạt cả 9 ngưỡng đã ký; sửa `business.cost_budget_per_ticket_vnd` từ 7500 về 1500 (trần tiền máy).

Vòng 2 (thẻ S7)
- Cố định LF cho các file bị khoá (`lab10/`, `data/`, `incidents/`, `tests/`) để kiểm toàn vẹn đạt trên Windows.
- C1: cổng pháp lý vòng 1 đã đưa số lần lộ PII của S7 về 0; dòng còn lỗi duy nhất là thiếu chỉ số mới trong `monitors.py`.
- C3.3 hiệu chỉnh lòng tin cho người đặt hàng và người nhận quà; C4 HAZOP của thẻ trên `notify_carrier` (4 dòng, có nhánh chưa thấy trên trace); câu 3.3 giả định môi trường về chữ khách gõ và người nhận đơn quà.
- C7 phần `legal`: thêm 8 tên trường dự phòng vào `pii_fields_blocked_to_third_party`, ghi rõ đây là GIẢM khả năng (chặn theo tên), còn NGĂN cần cổng danh sách cho phép theo `carrier_notice_fields`; `operations` không đổi, có số report làm căn cứ.
- C10 risk register: 2 dòng (dữ liệu người nhận lọt qua cổng chặn theo tên, PIC NV-TUNG, MANAGE; cổng chặn dữ liệu đẩy ca sang người duyệt, PIC NV-HANH, MEASURE), mỗi dòng có metric và ảnh hưởng tới v2.
- C11: cập nhật checklist 6 nhóm việc có PIC; Runbook 4 sau sự cố (tín hiệu lẽ ra báo trước, báo hãng, người nhận, Pháp chế, dữ liệu không thu hồi được); Runbook 5 ba kịch bản tuần đầu.
- Soát bài vòng 2 của các thành viên (câu 3.2, C6, C8), khớp nhãn nhánh giữa C6 và C7, gộp nhánh bị xung đột.

### Bằng chứng

Commit vòng 1: `7f1ea9c` (thông tin nhóm), `ce077b4` (câu 1.4), `a3f99aa` (câu 1.2), `fee7aea` (khôi phục Phiếu A), `02bfbf5` (sửa câu 1.3), `0c5a8a5` và `649385a` (đưa tiêu chí sang `main`, ký), `4e53b41` (HAZOP, checklist, câu 2.10, runbook), `0ff1845` (A5, `submission.json`), `173a9ae` (pre-mortem vận hành, pháp lý), `8c54763` (câu 2.8), `ad1333e` (gộp nhánh, sửa trần chi phí), `aec23b7` (v1).
Commit vòng 2: `4fac920` (LF cho file bị khoá), `ee2a487` (C1, C3.3, C4), `3606740` (câu 3.3), `6f86b99` (C7 legal, operations), `478edf0` (C10), `bfa53d8` (khớp nhãn C7 với C6), `a395a94` (C11).
Mã lần chạy: `R-base-prepared-20261119-200438-604cca` (prepared bộ nền), `R-S7-prepared-20261119-201750-604cca` (prepared S7), `R-S7-grade-20261119-201749-604cca` (tự kiểm tra S7), `R-S7-after-20261119-203925-5aede3` và `R-base-after-20261119-203926-5aede3` (sau khi sửa cổng pháp lý).

Commit `0a73cc0`, `73befa2`, `c1f2d33` cũng mang email `2A202603839@example.com` nhưng là phần việc của Hồ Anh Tú (cấu hình Git lúc đầu dùng chung máy).

Có dùng trợ lý AI (Claude Code) để đọc code của lab, viết nháp câu 1.2, 1.4, HAZOP, checklist, runbook, risk register, các mục Phiếu C và soát các nhánh trước khi merge; mọi con số và quyết định đã được đối chiếu với `data/world.json`, `lab10/` và report, và do tôi chốt.

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
