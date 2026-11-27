so_gio = float(input("Nhập số giờ làm việc hàng tuần: "))
luong_gio = float(input("Nhập mức lương theo giờ tiêu chuẩn: "))

GIO_CHUAN = 44

if so_gio > GIO_CHUAN:
    luong_thuc_nhan = GIO_CHUAN * luong_gio + (so_gio - GIO_CHUAN) * luong_gio * 1.5
else:
    luong_thuc_nhan = so_gio * luong_gio

print("Số tiền thực nhận của nhân viên là:", luong_thuc_nhan)
