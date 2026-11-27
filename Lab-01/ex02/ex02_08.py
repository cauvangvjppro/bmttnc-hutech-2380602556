nhap = input("Nhập chuỗi số nhị phân 4 chữ số, phân cách bằng dấu phẩy: ")
cac_so = nhap.split(",")

ket_qua = []
for so in cac_so:
    so = so.strip()
    if int(so, 2) % 5 == 0:
        ket_qua.append(so)

print(",".join(ket_qua))
