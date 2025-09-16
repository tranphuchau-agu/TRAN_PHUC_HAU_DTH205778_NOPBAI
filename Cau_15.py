# Giải thích cách chạy các dòng lệnh range
# (a) range(5) 
# (b) range(5, 10) 
# (c) range(5, 20, 3) 
# (d) range(20, 5, -1) 
# (e) range(20, 5, -3) 
# (f) range(10, 5) 
# (g) range(0) 
# (h) range(10, 101, 10) 
# (i) range(10, -1, -1) 
# (j) range(-3, 4) 
# (k) range(0, 10, 1) 

print("Dòng lệnh (a):", list(range(5)))
print(" - Giải thích: Dòng lệnh (a) tạo ra một dãy số bắt đầu từ 0 đến 4 (không bao gồm 5). Vì vậy, kết quả là [0, 1, 2, 3, 4].", end='\n\n')

print("Dòng lệnh (b):", list(range(5, 10)))
print(" - Giải thích: Dòng lệnh (b) tạo ra một dãy số bắt đầu từ 5 đến 9 (không bao gồm 10). Vì vậy, kết quả là [5, 6, 7, 8, 9].", end='\n\n')

print("Dòng lệnh (c):", list(range(5, 20, 3)))
print(" - Giải thích: Dòng lệnh (c) tạo ra một dãy số bắt đầu từ 5 đến 19 (không bao gồm 20) với bước nhảy là 3. Vì vậy, kết quả là [5, 8, 11, 14, 17].", end='\n\n')

print("Dòng lệnh (d):", list(range(20, 5, -1)))
print(" - Giải thích: Dòng lệnh (d) tạo ra một dãy số bắt đầu từ 20 đến 6 (không bao gồm 5) với bước nhảy là -1. Vì vậy, kết quả là [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6].", end='\n\n')

print("Dòng lệnh (e):", list(range(20, 5, -3)))
print(" - Giải thích: Dòng lệnh (e) tạo ra một dãy số bắt đầu từ 20 đến 6 (không bao gồm 5) với bước nhảy là -3. Vì vậy, kết quả là [20, 17, 14, 11, 8].", end='\n\n')

print("Dòng lệnh (f):", list(range(10, 5)))
print(" - Giải thích: Dòng lệnh (f) không tạo ra bất kỳ số nào vì bắt đầu từ 10 và kết thúc ở 5 với bước nhảy mặc định là 1 (tăng dần). Do đó, kết quả là một danh sách rỗng [].", end='\n\n')

print("Dòng lệnh (g):", list(range(0)))
print(" - Giải thích: Dòng lệnh (g) không tạo ra bất kỳ số nào vì bắt đầu và kết thúc đều là 0. Do đó, kết quả là một danh sách rỗng [].", end='\n\n')

print("Dòng lệnh (h):", list(range(10, 101, 10)))
print(" - Giải thích: Dòng lệnh (h) tạo ra một dãy số bắt đầu từ 10 đến 100 (không bao gồm 101) với bước nhảy là 10. Vì vậy, kết quả là [10, 20, 30, 40, 50, 60, 70, 80, 90, 100].", end='\n\n')

print("Dòng lệnh (i):", list(range(10, -1, -1)))
print(" - Giải thích: Dòng lệnh (i) tạo ra một dãy số bắt đầu từ 10 đến 0 (không bao gồm -1) với bước nhảy là -1. Vì vậy, kết quả là [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0].", end='\n\n')

print("Dòng lệnh (j):", list(range(-3, 4)))
print(" - Giải thích: Dòng lệnh (j) tạo ra một dãy số bắt đầu từ -3 đến 3 (không bao gồm 4). Vì vậy, kết quả là [-3, -2, -1, 0, 1, 2, 3].", end='\n\n')

print("Dòng lệnh (k):", list(range(0, 10, 1)))
print(" - Giải thích: Dòng lệnh (k) tạo ra một dãy số bắt đầu từ 0 đến 9 (không bao gồm 10) với bước nhảy là 1. Vì vậy, kết quả là [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].", end='\n\n')