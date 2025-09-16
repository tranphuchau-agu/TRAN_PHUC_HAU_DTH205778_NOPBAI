# Tính dãy số S(x, n) = x + x^2/2! + x^3/3! + ... + x^n/n!
import math

print("Tính dãy số S(x, n) = x + x^2/2! + x^3/3! + ... + x^n/n!\n")
x = float(input("Nhập vào x: "))
n, S = -1, 0
while n < 1:
    n = int(input("Nhập vào n (n ≥ 1): "))
for i in range(1, n + 1):
    S += x**i / math.factorial(i)
print(f"S({x}, {n}) = {S}")
