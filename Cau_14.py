# Có bao nhiêu dấu * được in ra trong khi thực thi vòng lặp while
a = 0
count = 0
while a < 100:
    b = 0
    while b < 40:
        if (a + b) % 2 == 0:
            print('*', end='')
            count += 1
        b += 1
    print()
    a += 1
print(f'\nTổng số dấu * được in ra là: {count}')