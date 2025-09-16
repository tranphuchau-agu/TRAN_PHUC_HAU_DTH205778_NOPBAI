# Nhập giá trị 2 số a, b theo phép toán do người dùng nhập vào
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
op = input("Nhập phép toán (+, -, *, /): ")
while op not in ['+', '-', '*', '/']:
    print("Phép toán không hợp lệ. Vui lòng nhập lại.")
    op = input("Nhập phép toán (+, -, *, /): ")
if op == '+':
    rs = a + b
elif op == '-':
    rs = a - b
elif op == '*':
    rs = a * b
elif op == '/':
    if b != 0:
        rs = a / b
    else:
        rs = "Lỗi: Không thể chia một số cho 0 !"
    