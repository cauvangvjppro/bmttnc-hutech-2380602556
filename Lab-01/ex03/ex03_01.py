# Câu 01: Tính tổng của tất cả các số chẵn trong một List
nhap = input("Nhập danh sách các số, phân cách bằng dấu phẩy: ")
danh_sach = [int(so.strip()) for so in nhap.split(",")]

tong_chan = 0
for so in danh_sach:
    if so % 2 == 0:
        tong_chan += so

print("Danh sách đã nhập:", danh_sach)
print("Tổng các số chẵn:", tong_chan)
