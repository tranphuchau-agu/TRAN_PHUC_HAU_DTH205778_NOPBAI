##Câu 1: Kiểm tra năm nhuần
print("Chương trình kiểm tra năm nhuần")
year=int(input("Nhập vào 1 năm đi: "))
if( year%4 == 0 and year%100 != 0) or year%400 == 0:
    print("Năm",year, "là năm nhuần đó!")
else:
    print("Năm",year, "không nhuần")
print("\n")

##Câu 2: Đếm số ngày trong tháng
print("Chương trình đếm số ngày trong tháng")
month=int(input("Nhập vào 1 tháng đi: "))
if month in (1,3,5,7,8,10,12):
    print("Tháng",month,"có 31 ngày")
elif month in (4,6,9,11):
    print("Tháng",month,"có 30 ngày")
elif month == 2:
    year=(int(input("Nhập năm nào đi bạn: ")))
    if( year%4==0 and year%100!=0 ) or year%400==0:
        print("Tháng",month,"có 29 ngày")
    else:
        print("Tháng",month,"có 28 ngày")
else:
    print("Tháng",month,"không hợp lệ!")
print("\n")

##Câu 3: Phương trình bậc 2
from math import sqrt
print("Chương trình Giải phương trình bậc 2")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
if a==0: #bx+c
    if b==0 and c==0:
        print("Vô số nghiệm")
    if b==0 and c!=0:
        print("Vô nghiệm")
    else:
        x = -c/b
        print("Nghiệm x =",x)
else:
    delta = b*b - 4*a*c
    if delta < 0:
        print("Vô nghiệm")
    elif delta == 0:
        x = -b / 2*a
        print("Nghiệm kép x1=x2=",x)
    else:
        x1 = ( -b - sqrt(delta) ) / 2*a
        x2 = ( -b + sqrt(delta) ) / 2*a
        print("Nghiệm x1 =",x1)
        print("Nghiệm x2 =",x2)
print("\n")

##Câu 4:
x = 3
y = 5
z = 7

print("(a)", x == 3)
print("(b)", x < y)
print("(c)", x >= y)
print("(d)", x <= y)
print("(e)", x != y - 2)
print("(f)", x < 10)
print("(g)", x >= 0 and x < 10)
print("(h)", x < 0 and x < 10)
print("(i)", x >= 0 and x < 2)
print("(j)", x < 0 or x < 10)
print("(k)", x > 0 or x < 10)
print("(l)", x < 0 or x > 10)

##Câu 5:
cases = {
    "a": (3, 5, 7),
    "b": (3, 7, 5),
    "c": (5, 3, 7),
    "d": (5, 7, 3),
    "e": (7, 3, 5),
    "f": (7, 5, 3),
}
for name, (i, j, k) in cases.items():
    if i < j:
        if j < k:
            i = j
        else:
            j = k
    else:
        if j > k:
            j = i
        else:
            i = k
    print(f"({name}) i = {i}, j = {j}, k = {k}")


##Câu 6
while True:
    n = int(input("Nhập số nguyên n (tối đa 2 chữ số): "))
    if 0 <= n <= 99:
        break
    print("Số không hợp lệ, vui lòng nhập lại!")

doc_so = ["không", "một", "hai", "ba", "bốn", 
          "năm", "sáu", "bảy", "tám", "chín"]

doc_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", 
            "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]

if n < 10:
    print(doc_so[n])
else:
    hchuc = n // 10
    dv = n % 10
    if dv == 0:
        print(doc_chuc[hchuc])
    elif dv == 1:
        print(doc_chuc[hchuc], "mốt")
    elif dv == 5:
        print(doc_chuc[hchuc], "lăm")
    else:
        print(doc_chuc[hchuc], doc_so[dv])


##Câu 7:
while True:
    d = int(input("Nhập ngày: "))
    if d <1 or d >31 :
        print("Ngày không hợp lệ, nhập lại!")
    else:
        break

while True:
    m = int(input("Nhập tháng: "))
    if m < 1 or m > 12:
        print("Tháng không hợp lệ, nhập lại!")
    elif d == 31 and m in (4, 6, 9, 11):
        print(f"Tháng {m} không có 31 ngày, nhập lại!")
    elif m == 2 and d > 29:
        print("Tháng 2 chỉ có tối đa 29 ngày, nhập lại!")
    else:
        break

while True:
    y = int(input("Nhập năm: "))
    if m == 2 and d == 29:
        if (y % 4 != 0) or (y % 100 == 0 and y % 400 != 0):
            print(f"Năm {y} không nhuận, vui lòng nhập lại!")
        else:
            break
    else:
        break

print(f"Bạn vừa nhập: {d:02d}/{m:02d}/{y}")
print("Ngày hôm sau là:", end=" ")

if d == 31 and m == 12:
    print(f"01/01/{y+1}")
elif m == 2 and d in (28, 29):
    print(f"01/03/{y}")
elif d == 30 and m in (4, 6, 9, 11):
    print(f"01/{m+1}/{y}")
elif d == 31 and m in (1, 3, 5, 7, 8, 10):
    print(f"01/{m+1}/{y}")
else:
    print(f"{d+1}/{m}/{y}")

##Câu 8:
x = float(input("Nhập số thứ nhất: "))
y = float(input("Nhập số thứ hai: "))
pt = input("Nhập phép toán (+, -, *, /): ")

if pt == "+":
    print("Kết quả:", x + y)
elif pt == "-":
    print("Kết quả:", x - y)
elif pt == "*":
    print("Kết quả:", x * y)
elif pt == "/":
    if y != 0:
        print("Kết quả:", x / y)
    else:
        print("Không thể chia cho 0!")
else:
    print("Phép toán không hợp lệ!")

##Câu 9:
month = int(input("Nhập số tháng (1-12): "))

if 1 <= month <= 3:
    print("Tháng này thuộc quý 1")
elif 4 <= month <= 6:
    print("Tháng này thuộc quý 2")
elif 7 <= month <= 9:
    print("Tháng này thuộc quý 3")
elif 10 <= month <= 12:
    print("Tháng này thuộc quý 4")
else:
    print("Bạn nhập tháng không hợp lệ!")


