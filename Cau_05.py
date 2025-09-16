# In ra giá trị của i, j, k sau khi thực hiện các bộ giá trị khởi tạo khác nhau. 
class Method:
    def __init__(self, i, j, k):
            self.i = i
            self.j = j
            self.k = k
    def Execute(self):
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

ch = "a"

for index in range(6):
    if index == 0:
        i, j, k = 3, 5, 7
    elif index == 1:
        i, j, k = 3, 7, 5
    elif index == 2:
        i, j, k = 5, 3, 7
    elif index == 3:
        i, j, k = 5, 7, 3
    elif index == 4:
        i, j, k = 7, 3, 5
    else:
        i, j, k = 7, 5, 3
    print("(",chr(ord(ch) + index), ") i =", i, ", j =", j, ", k =", k, ".")
    Method(i, j ,k)
    print("\n——> i =", i, ", j =", j, ", k =", k, "\n\n")
    