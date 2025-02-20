# **Biến và kiểu dữ liệu trong Python**

## **Mục tiêu bài học:**
- Hiểu khái niệm về biến trong Python và cách khai báo biến.
- Nắm vững các kiểu dữ liệu cơ bản trong Python: `int`, `float`, `str`, `bool`.
- Biết cách tạo và sử dụng biến trong Python.

---

## **1. Biến trong Python**

### **1.1. Khái niệm biến**
- Biến là nơi lưu trữ giá trị trong bộ nhớ khi chương trình đang chạy.
- Trong Python, bạn không cần phải khai báo kiểu dữ liệu của biến như trong các ngôn ngữ khác (ví dụ: C, Java). Python tự động xác định kiểu dữ liệu của biến dựa trên giá trị mà bạn gán cho nó.

### **1.2. Cách khai báo biến**
Để khai báo một biến trong Python, bạn chỉ cần gán giá trị cho biến mà không cần khai báo kiểu dữ liệu trước. Ví dụ:
```python
x = 10  # Khai báo biến x với giá trị 10
name = "Alice"  # Khai báo biến name với giá trị chuỗi "Alice"
```

### **1.3. Quy tắc đặt tên biến**
- Tên biến phải bắt đầu bằng một chữ cái hoặc dấu gạch dưới (`_`), theo sau có thể là chữ cái, số hoặc dấu gạch dưới.
- Tên biến không được trùng với các từ khóa trong Python (như `if`, `else`, `while`, v.v.).
- Tên biến phân biệt chữ hoa chữ thường, ví dụ: `Age` và `age` là hai biến khác nhau.

---

## **2. Các kiểu dữ liệu cơ bản trong Python**

### **2.1. Kiểu dữ liệu `int` (Số nguyên)**
- Kiểu `int` dùng để biểu diễn các số nguyên (không có phần thập phân).
- Ví dụ:
  ```python
  age = 25  # Số nguyên
  ```

### **2.2. Kiểu dữ liệu `float` (Số thực)**
- Kiểu `float` dùng để biểu diễn các số thực (có phần thập phân).
- Ví dụ:
  ```python
  price = 19.99  # Số thực
  ```

### **2.3. Kiểu dữ liệu `str` (Chuỗi văn bản)**
- Kiểu `str` dùng để biểu diễn các chuỗi văn bản (các ký tự).
- Chuỗi có thể được bao quanh bởi dấu nháy đơn (`'`) hoặc dấu nháy kép (`"`).
- Ví dụ:
  ```python
  name = "Alice"  # Chuỗi văn bản
  greeting = 'Hello, World!'  # Chuỗi văn bản
  ```

### **2.4. Kiểu dữ liệu `bool` (Boolean)**
- Kiểu `bool` dùng để biểu diễn giá trị đúng/sai (True/False).
- Ví dụ:
  ```python
  is_active = True  # Giá trị đúng
  is_sunny = False  # Giá trị sai
  ```

---

## **3. Thực hành: Tạo và sử dụng biến trong Python**

### **3.1. Bài tập thực hành**
1. **Bài tập 1: Tạo và gán giá trị cho các biến**
   - Tạo các biến sau: `age`, `height`, `name`, `is_student`.
   - Gán các giá trị tương ứng:
     - `age` là một số nguyên (ví dụ: 20).
     - `height` là một số thực (ví dụ: 5.75).
     - `name` là một chuỗi (ví dụ: "John").
     - `is_student` là một giá trị boolean (True hoặc False).
   
   **Code mẫu:**
   ```python
   age = 20  # Kiểu int
   height = 5.75  # Kiểu float
   name = "John"  # Kiểu str
   is_student = True  # Kiểu bool
   ```

2. **Bài tập 2: In giá trị các biến**
   - Sau khi tạo và gán giá trị cho các biến, hãy in ra màn hình các giá trị này.

   **Code mẫu:**
   ```python
   print("Age:", age)
   print("Height:", height)
   print("Name:", name)
   print("Is student:", is_student)
   ```

3. **Bài tập 3: Tính toán với các kiểu dữ liệu**
   - Tính tổng `age` và `height` và in ra kết quả.
   - Kiểm tra nếu `age` là một số nguyên dương.

   **Code mẫu:**
   ```python
   total = age + height
   print("Total:", total)

   if age > 0:
       print("Age is a positive number.")
   ```

---

## **4. Tổng kết**
- **Biến** là cách chúng ta lưu trữ giá trị trong bộ nhớ khi lập trình.
- Các **kiểu dữ liệu cơ bản** trong Python bao gồm: `int` (số nguyên), `float` (số thực), `str` (chuỗi văn bản), và `bool` (giá trị đúng/sai).
- Python tự động nhận diện kiểu dữ liệu của biến khi bạn gán giá trị cho nó, giúp việc lập trình trở nên linh hoạt và dễ dàng hơn.

---
## Bài tập
### **Bài tập 1: Tạo và sử dụng biến**
1. **Mô tả bài tập:**
   - Tạo một biến `name` lưu trữ tên của bạn.
   - Tạo một biến `age` lưu trữ tuổi của bạn (kiểu `int`).
   - Tạo một biến `height` lưu trữ chiều cao của bạn (kiểu `float`).
   - Tạo một biến `is_student` lưu trữ trạng thái học sinh (True/False) (kiểu `bool`).
   - In ra các giá trị của các biến trên.

2. **Yêu cầu:**
   - In ra thông tin dưới dạng: `"Name: <name>, Age: <age>, Height: <height>, Is Student: <is_student>"`.

---

### **Bài tập 2: Tính toán với kiểu dữ liệu**
1. **Mô tả bài tập:**
   - Tạo một biến `length` lưu trữ chiều dài (kiểu `float`).
   - Tạo một biến `width` lưu trữ chiều rộng (kiểu `float`).
   - Tính diện tích của một hình chữ nhật bằng cách nhân `length` và `width` lại với nhau.
   - Tính chu vi của hình chữ nhật bằng cách cộng chiều dài và chiều rộng và nhân với 2.

2. **Yêu cầu:**
   - In ra kết quả diện tích và chu vi dưới dạng:
     - `"Area: <area>"`.
     - `"Perimeter: <perimeter>"`.

---

### **Bài tập 3: Kiểm tra số nguyên và số thực**
1. **Mô tả bài tập:**
   - Tạo một biến `num` lưu trữ một số nguyên.
   - Kiểm tra xem `num` có phải là một số nguyên dương hay không. Nếu đúng, in ra `"Positive integer"`. Nếu không, in ra `"Not a positive integer"`.
   - Tạo một biến `decimal` lưu trữ một số thực.
   - Kiểm tra xem `decimal` có phải là một số dương hay không. Nếu đúng, in ra `"Positive decimal number"`. Nếu không, in ra `"Not a positive decimal number"`.

2. **Yêu cầu:**
   - In ra kết quả tương ứng với từng kiểm tra.

---

### **Bài tập 4: Đổi giá trị giữa hai biến**
1. **Mô tả bài tập:**
   - Tạo hai biến `a` và `b` với các giá trị bất kỳ (kiểu `int`).
   - Đổi giá trị của `a` và `b` cho nhau mà không sử dụng biến phụ.
   - In ra giá trị của `a` và `b` sau khi đổi chỗ.

2. **Yêu cầu:**
   - In ra kết quả dưới dạng: `"a = <a>, b = <b>"` sau khi hoán đổi giá trị.

---

### **Bài tập 5: Sử dụng kiểu chuỗi (string)**
1. **Mô tả bài tập:**
   - Tạo một biến `sentence` lưu trữ một câu hoàn chỉnh.
   - Sử dụng các phương thức của chuỗi (như `upper()`, `lower()`, `replace()`) để thao tác với chuỗi này.
     - Chuyển toàn bộ câu thành chữ hoa.
     - Chuyển toàn bộ câu thành chữ thường.
     - Thay thế một từ nào đó trong câu với từ khác.

2. **Yêu cầu:**
   - In ra các kết quả của các thao tác với chuỗi.

---

### **Bài tập 6: Kiểu Boolean (True/False)**
1. **Mô tả bài tập:**
   - Tạo một biến `is_raining` (kiểu `bool`) để lưu trữ tình trạng thời tiết (True nếu đang mưa, False nếu không mưa).
   - Kiểm tra nếu `is_raining` là True, in ra `"Take an umbrella!"`, nếu False, in ra `"Enjoy the sunny day!"`.

2. **Yêu cầu:**
   - In ra kết quả dựa trên giá trị của `is_raining`.

---

### **Bài tập 7: Tính toán với các phép toán**
1. **Mô tả bài tập:**
   - Tạo một biến `num1` và `num2` là hai số nguyên.
   - Thực hiện các phép toán sau:
     - Cộng hai số.
     - Trừ hai số.
     - Nhân hai số.
     - Chia hai số (với kiểm tra chia cho 0).
   - In ra kết quả của từng phép toán.

2. **Yêu cầu:**
   - In ra kết quả dưới dạng:
     - `"Sum: <sum>"`.
     - `"Difference: <difference>"`.
     - `"Product: <product>"`.
     - `"Quotient: <quotient>"`.

---

### **Bài tập 8: Tạo và làm việc với danh sách**
1. **Mô tả bài tập:**
   - Tạo một danh sách `numbers` gồm 5 số nguyên bất kỳ.
   - Thêm một số vào cuối danh sách.
   - Xóa một số trong danh sách.
   - Sắp xếp danh sách theo thứ tự tăng dần.

2. **Yêu cầu:**
   - In ra danh sách sau khi thêm, xóa và sắp xếp.

---

### **Bài tập 9: Tạo một câu chuyện đơn giản**
1. **Mô tả bài tập:**
   - Tạo các biến `name`, `age`, `city` lưu trữ tên, tuổi và thành phố của bạn.
   - Dùng các biến này để tạo một câu chuyện đơn giản, ví dụ: `"My name is <name>. I am <age> years old and I live in <city>."`

2. **Yêu cầu:**
   - In ra câu chuyện với các biến được chèn vào.