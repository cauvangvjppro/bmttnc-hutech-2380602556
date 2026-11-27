# Câu 01: Tính tổng của tất cả các số chẵn trong một List
nhap = input("Enter a list of numbers separated by commas: ")
danh_sach = [int(so.strip()) for so in nhap.split(",")]

tong_chan = 0
for so in danh_sach:
    if so % 2 == 0:
        tong_chan += so

print("List entered:", danh_sach)
print("Sum of even numbers:", tong_chan)
