print("Nhập các dòng chuỗi (nhập dòng trống để kết thúc):")
cac_dong = []
while True:
    dong = input()
    if dong == "":
        break
    cac_dong.append(dong.upper())

for dong in cac_dong:
    print(dong)
