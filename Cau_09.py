i1 = 2 
i2 = 5 
i3 = -3 
d1 = 2.0 
d2 = 5.0 
d3 = -0.5

print("Kết quả các phép tính:\n")
n = i1 + (i2 * i3)
print("(a) i1 + (i2 * i3) = ", n)  # Kết quả là -13
print("(a) Thực hiện i2 * i3 trước vì phép nhân (*) có ưu tiên cao hơn phép cộng (+)\n")
n = i1 * (i2 + i3)
print("(b) i1 * (i2 + i3) = ", n)  # Kết quả là 4
print("(b) Thực hiện (i2 + i3) trước vì trong ngoặc có ưu tiên cao nhất\n")
n = i1 / (i2 + i3)
print("(c) i1 / (i2 + i3) = ", n)  # Kết quả là 1.0
print("(c) Thực hiện (i2 + i3) trước vì trong ngoặc có ưu tiên cao nhất\n")
n = i1 // (i2 + i3)
print("(d) i1 // (i2 + i3) = ", n)  # Kết quả là 1
print("(d) Thực hiện (i2 + i3) trước vì trong ngoặc có ưu tiên cao nhất\n")
n =i1 / i2 + i3
print("(e) i1 / i2 + i3 = ", n)  # Kết quả là -2.6
print("(e) Thực hiện i1 / i2 trước vì phép chia (/) có ưu tiên cao hơn phép cộng (+)\n")
n = i1 // i2 + i3
print("(f) i1 // i2 + i3 = ", n)  # Kết quả là -3
print("(f) Thực hiện i1 // i2 trước vì phép chia lấy phần nguyên (//) có ưu tiên cao hơn phép cộng (+)\n")
n = 3 + 4 + 5 / 3
print("(g) 3 + 4 + 5 / 3 = ", n)  # Kết quả là 8.666666666666666
print("(g) Thực hiện 5 / 3 trước vì phép chia (/) có ưu tiên cao hơn phép cộng (+)\n")
n = 3 + 4 + 5 // 3
print("(h) 3 + 4 + 5 // 3 = ", n)  # Kết quả là 10
print("(h) Thực hiện 5 // 3 trước vì phép chia lấy phần nguyên (//) có ưu tiên cao hơn phép cộng (+)\n")
n = (3 + 4 + 5) / 3
print("(i) (3 + 4 + 5) / 3 = ", n)  # Kết quả là 4.0
print("(i) Thực hiện (3 + 4 + 5) trước vì trong ngoặc có ưu tiên cao nhất\n")
n = (3 + 4 + 5) // 3
print("(j) (3 + 4 + 5) // 3 = ", n)  # Kết quả là 4
print("(j) Thực hiện (3 + 4 + 5) trước vì trong ngoặc có ưu tiên cao nhất\n")
n = d1 + (d2 * d3)
print("(k) d1 + (d2 * d3) = ", n)  # Kết quả là -0.5
print("(k) Thực hiện (d2 * d3) trước vì trong ngoặc có ưu tiên cao nhất\n")
n = d1 + d2 * d3
print("(l) d1 + d2 * d3 = ", n)  # Kết quả là -0.5
print("(l) Thực hiện d2 * d3 trước vì phép nhân (*) có ưu tiên cao hơn phép cộng (+)\n")
n = d1 / d2 - d3
print("(m) d1 / d2 - d3 = ", n)  # Kết quả là 0.9
print("(m) Thực hiện d1 / d2 trước vì phép chia (/) có ưu tiên cao hơn phép trừ (-)\n")
n = d1 / (d2 - d3)
print("(n) d1 / (d2 - d3) = ", n)  # Kết quả là 0.4444444444444444
print("(n) Thực hiện (d2 - d3) trước vì trong ngoặc có ưu tiên cao nhất\n")
n = d1 + d2 + d3 / 3
print("(o) d1 + d2 + d3 / 3 = ", n)  # Kết quả là 6.833333333333333
print("(o) Thực hiện d3 / 3 trước vì phép chia (/) có ưu tiên cao hơn phép cộng (+)\n")
n = (d1 + d2 + d3) / 3
print("(p) (d1 + d2 + d3) / 3 = ", n)  # Kết quả là 2.8333333333333335
print("(p) Thực hiện (d1 + d2 + d3) trước vì trong ngoặc có ưu tiên cao nhất\n")
n = d1 + d2 + (d3 / 3)
print("(q) d1 + d2 + (d3 / 3) = ", n)  # Kết quả là 6.833333333333333
print("(q) Thực hiện (d3 / 3) trước vì trong ngoặc có ưu tiên cao nhất\n")
n = 3 * (d1 + d2) * (d1 - d3) 
print("(r) 3 * (d1 + d2) * (d1 - d3) = ", n)  # Kết quả là 63.0
print("(r) Thực hiện (d1 + d2) và (d1 - d3) trước vì trong ngoặc có ưu tiên cao nhất\n")