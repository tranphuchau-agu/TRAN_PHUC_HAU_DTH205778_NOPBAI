# Các loại lỗi khi lập trình Python và cách bắt lỗi

# 1. Lỗi cú pháp (SyntaxError)
# Xảy ra khi mã nguồn không tuân thủ cú pháp Python.
# Ví dụ:
# print("Hello World"  # thiếu dấu đóng ngoặc

# 2. Lỗi thực thi (Runtime Error)
# Xảy ra khi chương trình chạy, ví dụ chia cho 0, truy cập biến chưa khai báo.
# Ví dụ:
# x = 1 / 0  # ZeroDivisionError

# 3. Lỗi logic (Logic Error)
# Chương trình chạy nhưng kết quả không đúng như mong muốn.
# Ví dụ:
# def tinh_tong(a, b):
#     return a - b  # sai logic, phải là a + b

# Cách bắt lỗi trong Python: sử dụng khối try-except

try:
    x = int(input("Nhập số: "))
    y = 10 / x
    print("Kết quả:", y)
except ValueError:
    print("Lỗi: Bạn phải nhập một số nguyên.")
except ZeroDivisionError:
    print("Lỗi: Không được chia cho 0.")
except Exception as e:
    print("Lỗi khác:", e)
finally:
    print("Kết thúc chương trình.")

# Có thể tự định nghĩa lỗi bằng cách kế thừa Exception
class MyError(Exception):
    pass

try:
    raise MyError("Đây là lỗi tự định nghĩa!")
except MyError as e:
    print(e)