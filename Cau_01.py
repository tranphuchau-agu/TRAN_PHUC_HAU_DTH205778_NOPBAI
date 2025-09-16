import math

try:
    r = float(input('Nhap ban kinh: '))
    cv = 2 * math.pi * r
    dt = r**2
    print(f'Chu vi hinh tron: {cv}')
    print(f'Dien tich hinh tron: {dt}')
except:
    print('Ban kinh khong hop le!')