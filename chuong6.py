#Câu 1:
print("\nCâu 1:\n")
from random import randrange

print("Chương trình xử lý List")
n = int(input("Nhập số phần tử: "))
lst = [0] * n

for i in range(n):
    lst[i] = randrange(-100, 100)
    
print("List ngẫu nhiên là:")
print(lst)

print("Mời bạn thêm số mới:")
value = int(input())
lst.append(value)
print(lst)

print("Bạn muốn đếm số nào:")
k = int(input())
dem = lst.count(k)
print(k, "xuất hiện", dem, "lần trong list")

def CheckPrime(n):
    d = 0
    if n <= 1:
        return False
        
    for i in range(1, n + 1):
        if n % i == 0:
            d += 1
    return d == 2

demnt = 0
tongnt = 0

for x in lst:
    if CheckPrime(x):
        demnt += 1
        tongnt += x
        
print("Có ", demnt, "số nguyên tố trong list")
print("Tổng=", tongnt)

lst.sort()
print("List sau khi sort:")
print(lst)


del lst
print("List sau khi xóa:")

#Câu 2:
print("\nCâu 2:\n")
from random import randrange

lst = []
print("Nhập số phần tử:")
n = int(input())

for i in range(n):
    lst.append(randrange(0, 100))
    
print("List sau khi tạo ngẫu nhiên là:")
print(lst)

x = int(input("Mời bạn chèn thêm số mới: "))
lst.append(x)
print("List sau khi chèn:")
print(lst)

k = int(input("Mời nhập số để xóa: "))
while lst.count(k) > 0:
    lst.remove(k)
    
print("List sau khi xóa:")
print(lst)

def CheckDoiXung(lst):
    for i in range(len(lst)):
        if lst[i] != lst[len(lst) - i - 1]:
            return False
    return True

kt = CheckDoiXung(lst)
if kt == True:
    print("List đối xứng")
else:
    print("List không đối xứng")

#Câu 3:
print("\nCâu 3:\n")
from random import randrange

def TaoMaTran(m, n):
    D = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(randrange(100))
        D.append(row)
    return D

def XuatMaTran(D):
    for row in D:
        for element in row:
            print(element, end='\t')
        print()

def LayDong(r):
    R = D[r]
    return R

def XuatList1Chieu(R):
    for element in R:
        print(element, end='\t')
        
def LayCot(c):
    C = []
    for i in range(len(D)):
        C.append(D[i][c])
    return C

def MAX(D):
    max = D[0][0]
    for i in range(len(D)):
        for j in range(len(D[i])):
            if (max < D[i][j]):
                max = D[i][j]
    return max

print("Nhập số dòng:")
m = int(input())
print("Nhập số cột:")
n = int(input())

D = TaoMaTran(m, n)
XuatMaTran(D)

print("Mời bạn nhập dòng muốn xuất:")
r = int(input())
XuatList1Chieu(LayDong(r))

print("\nMời bạn nhập cột muốn xuất:")
c = int(input())
XuatList1Chieu(LayCot(c))

max = MAX(D)
print("\nSố lớn nhất trong ma trận=", max)

#Câu 4:
print("\nCâu 4:\n")
lst = [3, 0, 1, 5, 2]
x=2

print("lst[0] =", lst[0])
print("lst[3] =", lst[3])
print("lst[x] =", lst[x])
print("lst[-x] =", lst[-x])
print("lst[x+1] =", lst[x+1])
print("lst[x] + 1=", lst[x] + 1)
print("lst[lst[x]] =", lst[lst[x]])
print("lst[lst[lst[x]]] =", lst[lst[lst[x]]])

#Câu 5:
print("\nCâu 5:\n")
lst = [20, 1, -34, 40, -8, 60, 1, 3]

print("lst = ", lst)
print("lst[0:3] =", lst[0:3])
print("lst[4:8] =", lst[4:8])
print("lst[4:33] =", lst[4:33])
print("lst[-5:-3] =", lst[-5:-3])
print("lst[-22:3] =", lst[-22:3])
print("lst[4:] =", lst[4:])
print("lst[:] =", lst[:])
print("lst[:4] =", lst[:4])
print("-34 in lst =", -34 in lst)
print("-34 not in lst =", -34 not in lst)

#Câu 6:
print("\nCâu 6:\n")
print("\n")
lst = []
n = int(input("Nhập số lượng phần tử: "))
for i in range(n):
    print("Nhập phần tử thứ", i +1, ": ", end="")
    so = int(input())
    lst.append(so)
    while True:
        if lst[i] in lst[0:i]:
            print("Phần tử trùng, nhập lại!")
            lst.remove(so)
            lst.append(int(input("Nhập phần tử thứ" + str(i + 1) + ": ")))
        else:
            break
print(lst)