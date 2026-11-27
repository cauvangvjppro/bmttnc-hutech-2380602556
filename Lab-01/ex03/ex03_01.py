nhap = input("Nhap danh sach cac so, cach nhau boi dau phay: ")
danh_sach = [int(so.strip()) for so in nhap.split(",")]

tong_chan = 0
for so in danh_sach:
    if so % 2 == 0:
        tong_chan += so

print("Tong cac so chan trong danh sach la:", tong_chan)
