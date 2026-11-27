# Câu 02: Đảo ngược vị trí của các phần tử trong một danh sách
nhap = input("Enter list elements separated by commas: ")
danh_sach = [phan_tu.strip() for phan_tu in nhap.split(",")]

danh_sach.reverse()

print("Original list:", [phan_tu.strip() for phan_tu in nhap.split(",")])
print("Reversed list:", danh_sach)
