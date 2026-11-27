# Câu 04: Truy cập các phần tử đầu tiên và cuối cùng trong một Tuple
nhap = input("Nhập các phần tử của Tuple, phân cách bằng dấu phẩy: ")
tuple_du_lieu = tuple(phan_tu.strip() for phan_tu in nhap.split(","))

if len(tuple_du_lieu) == 0:
    print("Tuple rỗng, không có phần tử nào.")
else:
    print("Tuple:", tuple_du_lieu)
    print("Phần tử đầu tiên:", tuple_du_lieu[0])
    print("Phần tử cuối cùng:", tuple_du_lieu[-1])
