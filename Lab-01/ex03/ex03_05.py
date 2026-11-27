nhap = input("Nhap danh sach cac phan tu, cach nhau boi dau phay: ")
danh_sach = [phan_tu.strip() for phan_tu in nhap.split(",")]

dem_so_lan = {}
for phan_tu in danh_sach:
    if phan_tu in dem_so_lan:
        dem_so_lan[phan_tu] += 1
    else:
        dem_so_lan[phan_tu] = 1

print("So luong xuat hien cua moi phan tu:", dem_so_lan)
