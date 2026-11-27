# Câu 02: Đảo ngược vị trí của các phần tử trong một danh sách
nhap = input("Nhập danh sách các phần tử, phân cách bằng dấu phẩy: ")
danh_sach = [phan_tu.strip() for phan_tu in nhap.split(",")]

danh_sach.reverse()

print("Danh sách ban đầu:", [phan_tu.strip() for phan_tu in nhap.split(",")])
print("Danh sách sau khi đảo ngược:", danh_sach)
