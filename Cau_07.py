
# Viết chương trình nhập vào ngày, tháng, năm và in ra ngày kế tiếp.
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    def next_day(self):
        if self.day < 30:
            self.day += 1
        else:
            self.day = 1
            if self.month < 12:
                self.month += 1
            else:
                self.month = 1
                self.year += 1

print("Nhập ngày, tháng, năm:")
day = int(input("\tNgày : "))
month = int(input("\tTháng: "))
year = int(input("\tNăm  : "))
date = Date(day, month, year)
date.next_day()
print("Ngày kế tiếp là: {}/{}/{}".format(date.day, date.month, date.year))