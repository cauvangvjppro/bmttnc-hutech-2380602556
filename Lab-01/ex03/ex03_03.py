nhap = input("Nhap danh sach cac phan tu, cach nhau boi dau phay: ")
danh_sach = [phan_tu.strip() for phan_tu in nhap.split(",")]

tuple_tu_danh_sach = tuple(danh_sach)

print("Tuple:", tuple_tu_danh_sach)
