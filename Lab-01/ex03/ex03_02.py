nhap = input("Nhap danh sach cac phan tu, cach nhau boi dau phay: ")
danh_sach = [phan_tu.strip() for phan_tu in nhap.split(",")]

danh_sach_dao_nguoc = danh_sach[::-1]

print("Danh sach sau khi dao nguoc:", danh_sach_dao_nguoc)
