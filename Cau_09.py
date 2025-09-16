month = -1
while month < 1 or month > 12:
    month = int(input("Nhập số tháng trong năm (1-12): "))

if month in [1, 2, 3]:
    season = "Quý 1"
elif month in [4, 5, 6]:
    season = "Quý 2"
elif month in [7, 8, 9]:
    season = "Quý 3"
else:
    season = "Quý 4"
print(f"Tháng {month} thuộc {season}.")