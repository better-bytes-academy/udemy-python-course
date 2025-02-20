# Cài đặt môi trường lập trình

## 1. Cài đặt Python và IDE (VSCode, PyCharm, v.v.)
Để bắt đầu lập trình với Python, bạn cần cài đặt Python trên máy tính của mình. Dưới đây là hướng dẫn cài đặt Python và một số IDE phổ biến:

- **Cài đặt Python**:
  1. Truy cập trang chủ của Python tại [python.org](https://www.python.org/downloads/).
  2. Tải về phiên bản Python mới nhất dành cho hệ điều hành của bạn (Windows, macOS, Linux).
  3. Trong quá trình cài đặt, nhớ đánh dấu vào tùy chọn **"Add Python to PATH"** để Python được thêm vào biến môi trường.
  4. Hoàn tất cài đặt và kiểm tra bằng cách mở terminal (hoặc Command Prompt trên Windows) và gõ lệnh:
     ```bash
     python --version
     ```
     Nếu Python được cài đặt thành công, bạn sẽ thấy thông tin phiên bản Python.

- **Cài đặt IDE (VSCode hoặc PyCharm)**:
  - **VSCode**:
    1. Truy cập [Visual Studio Code](https://code.visualstudio.com/) để tải và cài đặt.
    2. Sau khi cài đặt xong, mở VSCode và cài đặt extension **Python** từ marketplace để hỗ trợ lập trình Python.
  
  - **PyCharm**:
    1. Truy cập [PyCharm](https://www.jetbrains.com/pycharm/download/) và tải về phiên bản phù hợp.
    2. Cài đặt PyCharm theo hướng dẫn và mở PyCharm để bắt đầu lập trình Python.

## 2. Cách kiểm tra phiên bản Python trên máy
Sau khi cài đặt Python, bạn có thể kiểm tra xem Python đã được cài đặt đúng cách chưa và kiểm tra phiên bản đang sử dụng. Mở terminal (hoặc Command Prompt trên Windows) và nhập lệnh sau:
```bash
python --version
```
Hoặc:
```bash
python3 --version
```
Lệnh này sẽ hiển thị thông tin phiên bản Python mà bạn đã cài đặt. Nếu mọi thứ được cài đặt đúng cách, bạn sẽ thấy một kết quả tương tự như sau:
```
Python 3.x.x
```

## 3. Cài đặt công cụ hỗ trợ như pip (quản lý thư viện)
`pip` là công cụ quản lý thư viện trong Python, giúp bạn dễ dàng cài đặt và quản lý các thư viện bên ngoài (thư viện bổ sung) để sử dụng trong các dự án của mình. 

- **Kiểm tra pip**:
  Sau khi cài đặt Python, `pip` thường được cài đặt cùng. Bạn có thể kiểm tra phiên bản của pip bằng lệnh:
  ```bash
  pip --version
  ```
  Nếu pip đã được cài đặt đúng cách, lệnh này sẽ hiển thị phiên bản của pip.

- **Cài đặt thư viện bằng pip**:
  Để cài đặt một thư viện, bạn chỉ cần sử dụng lệnh:
  ```bash
  pip install <tên-thư-viện>
  ```
  Ví dụ, để cài đặt thư viện `requests`, bạn sử dụng lệnh:
  ```bash
  pip install requests
  ```

- **Cập nhật pip**:
  Để đảm bảo pip luôn được cập nhật, bạn có thể sử dụng lệnh sau để nâng cấp pip:
  ```bash
  python -m pip install --upgrade pip
  ```