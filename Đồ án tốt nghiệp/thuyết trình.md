# Báo cáo Đồ Án Tốt Nghiệp

**Chào Thầy, Cô và các bạn,**
Em là **Lê Nguyễn Duy Nghĩa**, sinh viên lớp 20SE4. Hôm nay, em rất vui được trình bày về đề tài đồ án tốt nghiệp của mình, đó là **Hệ thống chia sẻ thông tin dinh dưỡng và món ăn**.

## Lý do chọn đề tài

- Em nhận thấy các hệ thống hiện tại chỉ tập trung vào món ăn hoặc dinh dưỡng riêng lẻ, khiến người dùng gặp khó khăn nếu muốn tìm hiểu cả hai.
- Em muốn xây dựng một nền tảng giúp mọi người dễ dàng chia sẻ công thức nấu ăn, đồng thời cung cấp thông tin dinh dưỡng chi tiết để họ lập kế hoạch ăn uống và tập luyện, cải thiện sức khỏe.

## Ý nghĩa của hệ thống

- Mang lại tiện ích trong cuộc sống, nâng cao nhận thức về sức khỏe.
- Giao diện được thiết kế đơn giản, dễ sử dụng, tích hợp tính năng chặn bài viết có hình ảnh nhạy cảm, tính chỉ số BMI, TDEE.
- Tăng tương tác qua các diễn đàn và bài viết, tạo nên một cộng đồng chia sẻ và học hỏi lẫn nhau.

## Trong dự án có 3 role: người dùng đại trà, đầu bếp, người viết bài, người kiểm duyệt, admin

- Về role `người dùng đại trà`: có thể xem các bài post trên diễn đàn, có thể like, share, comment các bài viết đó, có thể báo cáo bài viết nếu như user đó phát hiện bài viết vi phạm tiêu chuẩn cộng đồng. Ngoài xem bài post thì user có thể xem 1 loạt các bài viết nấu ăn, chia sẽ dinh dưỡng thông qua mục album, người dùng có thể like, lưu, bình luận các bài viết trong album đó lun. Role này chỉ cho phép tạo post, không tạo được công thức nấu ăn, chia sẽ dinh dưỡng => chỉ được đọc thôi
- Role `đầu bếp`: về role này thì cũng có chức năng giống như role người dùng đại trà thôi, điểm đặc biệt để trở nên đầu bếp là thông qua các bài viết hướng dẫn nấu ăn, và chia sẽ dinh dưỡng, user đó được uy tín đạt được đủ follow của hệ thống yêu cầu (hiện tại thì em để nếu user đó có 3 người follow) thì sẽ lên được role đầu bếp. Điểm khác biệt của role này với role user bình thường là, có thể tạo các bài viết nấu ăn, tạo album, tạo blog dinh dưỡng
- Role `người viết bài`: role này thì được tạo từ account admin, có thể xem danh sách các bài viết đã tạo trước đó, tạo bài viết, chỉnh sửa bài viết, và tạo nguyên vật liệu cho phần dinh dưỡng
- Role `người kiểm duyệt`: khi các đầu bếp chia sẽ bài viết nấu ăn, tạo album thì sẽ chưa được đăng lên diễn đàn ngay lập tức, mà phải thông qua role người duyệt bài, nếu đồng ý thì bài viết đó mới được public trên diễn đàn
- Role `admin`: role này là quan trọng nhất của hệ thống, có thể xem thống kê trang web mình có bao nhiêu `user`, bao nhiêu `đầu bếp`, bao nhiêu `người viết bài`, bao nhiêu `người kiểm duyệt`.
- Muốn có được role người viết bài, và role người kiểm duyệt thì phải báo cáo qua admin, admin sẽ tạo account cho role đó, chứ không thể tự động tạo tài khoản theo cách thông thường được

## Về cách hoạt động

Hệ thống áp dụng mô hình **MVC (Model-View-Controller)**:

- **Model**: Quản lý dữ liệu như người dùng, bài viết, lịch ăn uống và tập luyện, sử dụng MongoDB đảm bảo khả năng truy xuất nhanh chóng và hiệu quả.
- **View**: Xây dựng bằng ReactJS, cung cấp giao diện trực quan, thân thiện với các tính năng chính như diễn đàn, lập lịch, và tìm kiếm bằng hình ảnh.
- **Controller**: Kết nối giữa giao diện và dữ liệu, sử dụng NodeJS. Sử dụng framework ExpressJS để viết các API để trả về data cho phía Client gọi và render ra giao diện

# Hệ Thống Hoạt Động Như Thế Nào?

1. **Người dùng (Client 1, 2, 3):**

   - Người dùng truy cập hệ thống qua Internet bằng trình duyệt hoặc ứng dụng.

2. **NGINX:**

   - Nhận yêu cầu từ người dùng và chuyển đến các thành phần khác.
   - Phân phối:
     - Giao diện (React).
     - API (Node.js).
     - Kết nối thời gian thực (WebSocket).

3. **React (Frontend):**

   - Là giao diện người dùng, hiển thị nội dung và xử lý tương tác.

4. **Node.js API (Backend):**

   - Xử lý logic chính của hệ thống.
   - Giao tiếp với cơ sở dữ liệu MongoDB.
   - Hỗ trợ kết nối thời gian thực qua WebSocket.

5. **MongoDB (Cơ sở dữ liệu):**

   - Lưu trữ và quản lý dữ liệu của hệ thống.

6. **Amazon S3:**

   - Lưu trữ các tệp như hình ảnh, video mà người dùng tải lên.

7. **Amazon EC2:**
   - Chạy backend (Node.js) và frontend (React.js).

---

### Tóm tắt dễ hiểu:

- Người dùng gửi yêu cầu -> **NGINX** nhận và chuyển tiếp.
- **React** xử lý giao diện, **Node.js** xử lý logic.
- Dữ liệu lưu trong **MongoDB**.
- Tệp tải lên lưu ở **S3**.
- Tất cả chạy trên **EC2**.

## Kết quả đạt được

- Hệ thống đã đáp ứng tốt các yêu cầu cơ bản như quản lý thông tin bài viết, tính toán chỉ số sức khỏe, và kiểm soát nội dung bài đăng.
- Điểm nổi bật là khả năng tích hợp món ăn và dinh dưỡng trong một ứng dụng duy nhất, giúp người dùng tiết kiệm thời gian và sử dụng tiện lợi hơn.

## Hướng phát triển trong tương lai

- Điểm đạt được: Giao diện thân thiện, xử lý nghiệp vụ diễn đàn cơ bản (quản lý bài viết, dinh dưỡng, lịch tập, lịch ăn uống), và hỗ trợ tính toán chỉ số sức khỏe chính xác (BMI, sức khỏe).
- Tích hợp nổi bật: Kết hợp món ăn và dinh dưỡng trong một nền tảng duy nhất, khắc phục hạn chế của hệ thống cũ.
- Hướng phát triển: Cải thiện AI, thêm tìm kiếm hình ảnh (VGG19), kiểm soát nội dung không phù hợp, và hỗ trợ bài đăng kèm video.

**Cảm ơn Thầy, Cô và các bạn đã lắng nghe phần trình bày của em. Em rất mong nhận được ý kiến đóng góp để hoàn thiện hơn.**
