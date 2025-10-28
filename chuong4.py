##Câu 1:
print("\n")

import math

print("Chương trình tính diện tích Tam Giác:")
a = float(input("Nhập cạnh a>0: "))
b = float(input("Nhập cạnh b>0: "))
c = float(input("Nhập cạnh c>0: "))
if (a<=0 or b<=0 or c <=0) or (a+b)<=c or (a+c) <= b or (b+c) <= a:
    print("Tam Giác không hợp lệ!")
else:
    cv = a+b+c
    p = cv /2
    dt = math.sqrt(p*(p-a) * p*(p-b) * p*(p-c))
    print("Diện tích tam giác:", dt)

##Câu 2:
print("\n")

from random import randrange
while True:
 somay=randrange(1,101)
 solandoan=0
 win=False
 while solandoan<7:
     solandoan+=1
     songuoi=int(input("Máy đoán [1..100], mời bạn đoán:"))
     print("Bạn đoán lần thứ ",solandoan)
     if somay==songuoi:
        print("Chúc mừng bạn đoán đúng, số máy là=",somay)
        win=True
        break
     if somay>songuoi:
        print("Bạn đoán sai, số máy > số bạn")
     elif somay<songuoi:
         print("Bạn đoán sai, số máy < số bạn")
     if win==False:
       print("GAME OVER!, số máy =",somay)
     hoi=input("Tiếp không?")
     if hoi=="k":
          break
     print("Cám ơn bạn đã chơi Game!")

##Câu 3:
print("\n")

def BMI(cao, nang):
    return cao/nang

def PhanLoai(bmi):
    if bmi < 18.5:
        return "Gầy"
    elif bmi <=24.9:
        return "Bình thường"
    elif bmi <= 34.9:
        return "Hơi béo"
    elif bmi <= 34.9:
        return "Béo phì cấp độ 1"
    elif bmi <= 39.9:
        return "Béo phì cấp độ 2"
    else:
        return "Béo phì cấp độ 3"
    
def NguyCoBenh(bmi):
    if bmi < 18.5:
        return "Thấp"
    elif bmi <=24.9:
        return "Trung Bình"
    elif bmi <= 34.9:
        return "Cao"
    elif bmi <= 34.9:
        return "Cao"
    elif bmi <= 39.9:
        return "Rất cao"
    else:
        return "Rất cao"

cao = float(input("Nhập vào chiều cao: "))
nang = float(input("Nhập vào cân nặng: "))

bmi = BMI(cao, nang)
print("BMI của bạn:", bmi)
print("Phân loại của bạn: ", PhanLoai(bmi))
print("Nguy cơ bệnh của bạn: ", NguyCoBenh(bmi))

##Câu 4:
print("\n")


def ROI(dt,cp):
    return (dt - cp)/cp

def GoiYDauTu(roi):
    if roi >= 0.75:
        print("==> Nên đầu tư")
    else:
        print("==> Không nên đầu tư")

print("Chương trình tính ROI")
dt = int(input("Nhập doanh thu: "))
cp = int(input("Nhập chi phí: "))
roi = ROI(dt,cp)
print("Tỉ lệ ROI:", roi)
print("==>",GoiYDauTu(roi))

##Câu 5:
print("\n")


def Fibonacci(n):
    if n <=2:
        return 1
    else:
        return Fibonacci(n -1) + Fibonacci(n-2)
def dsFibonacci(n):
    for i in range(1, n+1, 1):
        print(Fibonacci(i), end='\t')

print(Fibonacci(9))

dsFibonacci(9)

##Câu 7:
print("\n")

import math

def TinhKhoangCach(x_A, y_A, x_B, y_B):
    
    binhPhuongChenhLechX = (x_B - x_A)**2
    binhPhuongChenhLechY = (y_B - y_A)**2
    
    return math.sqrt(binhPhuongChenhLechX + binhPhuongChenhLechY)

print("Chuong trinh tinh do dai doan thang AB")

print("\nNhap toa do Diem A:")
x_A = float(input("Hoanh do xA: "))
y_A = float(input("Tung do yA: "))

print("\nNhap toa do Diem B:")
x_B = float(input("Hoanh do xB: "))
y_B = float(input("Tung do yB: "))

doDaiAB = TinhKhoangCach(x_A, y_A, x_B, y_B)
print(f"\nDo dai canh |AB| = {doDaiAB:.4f}")

##Câu 8:
print("\n")

import math

def TinhLoga(soX, coSoA):
    return math.log(soX) / math.log(coSoA)

while True:
    try:
        soX = float(input("Nhap gia tri X: "))
        if soX > 0:
            break
        else:
            print("Loi: X phai lon hon 0. Nhap lai!")
    except ValueError:
        print("Loi: Du lieu nhap khong phai la so.")

while True:
    try:
        coSoA = float(input("Nhap co so A: "))
        if coSoA > 0 and coSoA != 1:
            break
        else:
            print("Loi: Co so A phai > 0 va A != 1. Nhap lai!")
    except ValueError:
        print("Loi: Du lieu nhap khong phai la so.")

ketQuaLogarit = TinhLoga(soX, coSoA)
print(f"Ket qua logarit co so {coSoA} cua {soX} la: {ketQuaLogarit}")

##Câu 9:
print("\n")

import math

def TinhDayCan(n_lan):
    
    if n_lan == 1:
        return math.sqrt(2)
    else:
        return math.sqrt(2 + TinhDayCan(n_lan - 1))

giaTriN = int(input("Nhap so lan lap (n): "))

ketQuaCuoi = TinhDayCan(giaTriN)
print(f"Gia tri S({giaTriN}) la: {ketQuaCuoi}")


