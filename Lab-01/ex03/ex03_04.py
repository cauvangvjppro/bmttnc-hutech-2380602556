nhap = input("Nhap cac phan tu cua Tuple, cach nhau boi dau phay: ")
tuple_du_lieu = tuple(phan_tu.strip() for phan_tu in nhap.split(","))

if len(tuple_du_lieu) == 0:
    print("Tuple rong.")
else:
    print("Phan tu dau tien:", tuple_du_lieu[0])
    print("Phan tu cuoi cung:", tuple_du_lieu[-1])
