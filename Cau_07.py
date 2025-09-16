# Cách 1: Nhập một chuỗi
name = input("Nhập tên của bạn: ")
print("Tên bạn là: ", name)

# Cách 2: Nhập một số nguyên
age = int(input("Nhập tuổi của bạn: "))
print("Tuổi bạn là: ", age)

# Cách 3: Nhập nhiều giá trị trên một dòng, cách nhau bởi dấu cách
a, b = input("Nhập hai số, cách nhau bởi dấu cách: ").split()
print("Số thứ nhất: ", a)
print("Số thứ hai : ", b)

# Cách 4: Nhập nhiều số và chuyển sang kiểu số nguyên
numbers = list(map(int, input("Nhập các số, cách nhau bởi dấu cách: ").split()))
print("Danh sách số vừa nhập: ", numbers)