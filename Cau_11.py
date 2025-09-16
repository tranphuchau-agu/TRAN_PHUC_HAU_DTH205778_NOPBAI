# Kiểm tra số nguyên tố
while True:
    n = int(input("Nhập n để kiểm tra số nguyên tố: "))
    if n < 2:
        print(f"{n} không phải số nguyên tố.")
        continue
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} không phải số nguyên tố.")
            break
    else:
        print(f"{n} là số nguyên tố.")
    while ch not in ('y', 'n'):
        ch = input("Bạn có muốn kiểm tra số khác không? (y/n): ").lower()
    if ch == 'y':
        continue