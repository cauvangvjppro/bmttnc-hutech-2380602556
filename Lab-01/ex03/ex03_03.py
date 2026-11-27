# Câu 03: Tạo một Tuple từ một List nhập vào từ bàn phím
nhap = input("Enter list elements separated by commas: ")
danh_sach = [phan_tu.strip() for phan_tu in nhap.split(",")]

tuple_tu_danh_sach = tuple(danh_sach)

print("List:", danh_sach)
print("Tuple:", tuple_tu_danh_sach)
