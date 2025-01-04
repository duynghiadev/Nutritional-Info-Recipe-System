# Lưu ý khi thêm bài viết vào album:

- Vào mục tạo bài viết nấu ăn -> tạo bài viết -> nhưng không được accpet bởi admin -> sau đó nhấp vào album mà mình muốn thêm bài viết -> bên phần bên phải có những bài viết chưa được admin duyệt -> mình bấm vào dấu + của bất kỳ bài viết nào -> thế là nó đã thêm vào album
- Sau đó vào account admin -> vào quản lý album -> duyệt bài viết -> sau khi duyệt xong thì quay lại account client đó -> vào xem album là sẽ có bài viết mình vừa được thêm vào

---

## Tính năng nhận diện ảnh nhạy cảm, quên password trong project:

- bấm **quên mật khẩu**, app nó gửi mail về, mình bấm xác thực -> chưa test
- khi post bài, upload ảnh có yếu tố **nhạy cảm** thì app phát hiện và toast lên thông báo đây là ảnh nhạy cảm, không cho upload (cái này dùng thư viện) -> trong file **`ModalUploadPost.jsx`** có hàm **`handleUpload`** này check -> đã test

---

- **Tiêu chí để nhận diện một hình ảnh là ảnh nhạy cảm:**
  - Sử dụng thư viện https://www.npmjs.com/package/nsfwjs
  - Khi sử dụng thư viện **nsfwjs** xác định các loại nội dung có thể gây nhạy cảm như: **Sexy**, **Porn**, hoặc **Hentai**.
  - Mỗi hình ảnh được phân tích bởi mô hình và trả về một tập hợp các dự đoán, trong đó mỗi dự đoán bao gồm tên loại nội dung (**className**) và xác suất (**probability**) xảy ra trong nội dung đó.
  - Để quyết định một hình ảnh có phải là nhạy cảm hay không, cần kiểm tra:
    - Tên loại nội dung: Nếu hình ảnh thuộc các loại nhạy cảm như **Sexy**, **Porn**, hoặc **Hentai**.
    - Xác suất: Nếu xác suất dự đoán của loại nhạy cảm đó vượt ngưỡng **60%**. => Nếu cả hai tiêu chí trên được đáp ứng, hình ảnh sẽ được coi là nhạy cảm và không cho phép tải lên.
