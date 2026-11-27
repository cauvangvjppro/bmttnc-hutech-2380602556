# Câu 05: Đếm số lần xuất hiện của mỗi phần tử trong một List và lưu vào Dictionary
nhap = input("Enter list elements separated by commas: ")
danh_sach = [phan_tu.strip() for phan_tu in nhap.split(",")]

dem_so_lan = {}
for phan_tu in danh_sach:
    if phan_tu in dem_so_lan:
        dem_so_lan[phan_tu] += 1
    else:
        dem_so_lan[phan_tu] = 1

print("List:", danh_sach)
print("Count of each element:", dem_so_lan)
