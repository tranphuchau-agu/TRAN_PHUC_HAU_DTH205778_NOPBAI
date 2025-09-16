# Tính nghiệm phương trình bậc hai: ax^2 + bx + c = 0
import math

print("Chương trình tính phương trình bậc hai: ax^2 + bx + c = 0\n")
a = float(input("Nhập hệ số a (a ≠ 0): "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
if a == 0:
    print("Hệ số a không được bằng 0.")
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phương trình vô nghiệm.")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Phương trình có nghiệm kép: x1 = x2 = {x}")
    else:
        sqrt_delta = math.sqrt(delta)
        x1 = (-b + sqrt_delta) / (2*a)
        x2 = (-b - sqrt_delta) / (2*a)
        print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}")