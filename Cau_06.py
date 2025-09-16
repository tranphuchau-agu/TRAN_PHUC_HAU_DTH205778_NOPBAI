# Viết chương trình nhập vào một số nguyên n (0 -> 100). In ra cách đọc của số nguyên n.
print("Nhập vào số nguyên n (1 -> 100): ")
n = int(input())
if (n < 0) or (n > 100):
    print("Số nhập vào không hợp lệ!")
else:
    if n == 0:
        print("Không")
    elif n == 100:
        print("Một trăm")
    elif n < 10:
        if n == 1:
            print("Một")
        elif n == 2:
            print("Hai")
        elif n == 3:
            print("Ba")
        elif n == 4:
            print("Bốn")
        elif n == 5:
            print("Năm")
        elif n == 6:
            print("Sáu")
        elif n == 7:
            print("Bảy")
        elif n == 8:
            print("Tám")
        elif n == 9:
            print("Chín")
    else:
        chuc = n // 10
        donvi = n % 10
        if chuc == 1:
            print("Mười")
        elif chuc == 2:
            print("Hai mươi")
        elif chuc == 3:
            print("Ba mươi")
        elif chuc == 4:
            print("Bốn mươi")
        elif chuc == 5:
            print("Năm mươi")
        elif chuc == 6:
            print("Sáu mươi")
        elif chuc == 7:
            print("Bảy mươi")
        elif chuc == 8:
            print("Tám mươi")
        elif chuc == 9:
            print("Chín mươi")

        if donvi == 1:
            print("mốt")
        elif donvi == 2:
            print("hai")
        elif donvi == 3:
            print("ba")
        elif donvi == 4:
            print("bốn")
        elif donvi == 5:
            print("năm")
        elif donvi == 6:
            print("sáu")
        elif donvi == 7:
            print("bảy")
        elif donvi == 8:
            print("tám")
        elif donvi == 9:
            print("chín")