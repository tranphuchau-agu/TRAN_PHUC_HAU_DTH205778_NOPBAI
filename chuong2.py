#Câu 1: Tính chu vi, diện tích hình tròn
import math
try:
    r  = float(input("Nhập bán kính hình tròn: "))
    cv = 2*math.pi*r
    dt = math.pi*r*r
    print("Chu vi hình tròn = ",cv)
    print("Điện tích hình tròn = ",dt)
except:
    print("Lỗi rồi!")


#Câu 2: Tính giờ phút giây
t = int(input("Nhập số giây: "))
gio = (t//3600) % 24
phut = (t%3600) // 60
giay = (t%3600) % 60
print(gio," giờ", phut, " phút", giay, " giây")


#Câu 3: Tính điểm trung bình Toán, Lý, Hóa
toan = float(input("Nhập điểm Toán: "))
ly = float(input("Nhập điểm Lý: "))
hoa = float(input("Nhập điểm Hóa: "))
dtb = (toan+ly+hoa) / 3
print("Điểm trung bình = ", dtb)
print("Điểm trung bình = ", round(dtb,2))

