# Câu 04: Truy cập các phần tử đầu tiên và cuối cùng trong một Tuple
nhap = input("Enter Tuple elements separated by commas: ")
tuple_du_lieu = tuple(phan_tu.strip() for phan_tu in nhap.split(","))

if len(tuple_du_lieu) == 0:
    print("Empty tuple, no elements.")
else:
    print("Tuple:", tuple_du_lieu)
    print("First element:", tuple_du_lieu[0])
    print("Last element:", tuple_du_lieu[-1])
