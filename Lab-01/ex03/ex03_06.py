# Câu 06: Xóa một phần tử từ Dictionary theo key đã cho
nhap = input("Nhập các cặp key:value cho Dictionary, phân cách bằng dấu phẩy (ví dụ: a:1,b:2): ")
dictionary = {}
for cap in nhap.split(","):
    key, value = cap.strip().split(":")
    dictionary[key.strip()] = value.strip()

print("Dictionary ban đầu:", dictionary)

key_xoa = input("Nhập key cần xóa: ")
if key_xoa in dictionary:
    del dictionary[key_xoa]
    print("Dictionary sau khi xóa key '{}':".format(key_xoa), dictionary)
else:
    print("Không tìm thấy key '{}' trong Dictionary.".format(key_xoa))
