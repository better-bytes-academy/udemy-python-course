# Bài tập 1: Tạo và sử dụng biến
name = "John Doe"
age = 25
height = 1.75
is_student = False
print(f"Name: {name}, Age: {age}, Height: {height}, Is Student: {is_student}")

# Bài tập 2: Tính toán với kiểu dữ liệu
length = 5.0
width = 3.0
area = length * width
perimeter = 2 * (length + width)
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")

# # Bài tập 3: Kiểm tra số nguyên và số thực
num = 10
if num > 0 and isinstance(num, int):
    print("Positive integer")
else:
    print("Not a positive integer")

decimal = 5.5
if decimal > 0:
    print("Positive decimal number")
else:
    print("Not a positive decimal number")

# Bài tập 4: Đổi giá trị giữa hai biến
a = 10
b = 20
a, b = b, a
print(f"a = {a}, b = {b}")

# Bài tập 5: Sử dụng kiểu chuỗi
sentence = "Hello, world!"
print(sentence)
print(sentence.upper())
print(sentence.lower())
print(sentence.replace("world", "Python"))

# # Bài tập 6: Kiểu Boolean
is_raining = True
if is_raining:
    print("Take an umbrella!")
else:
    print("Enjoy the sunny day!")

# # Bài tập 7: Tính toán với các phép toán
# num1 = 10
# num2 = 5
# print(f"Sum: {num1 + num2}")
# print(f"Difference: {num1 - num2}")
# print(f"Product: {num1 * num2}")
# if num2 != 0:
#     print(f"Quotient: {num1 / num2}")
# else:
#     print("Cannot divide by zero")

# # Bài tập 8: Tạo và làm việc với danh sách
# numbers = [10, 5, 8, 3, 7]
# numbers.append(12)
# numbers.remove(5)
# numbers.sort()
# print(numbers)

# Bài tập 9: Tạo một câu chuyện đơn giản
character = "Alice"
place = "wonderland"
action = "explored the mysterious forest"
story = f"One day, {character} went to {place} and {action}."
print(story)
