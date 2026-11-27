# Câu 06: Xóa một phần tử từ Dictionary theo key đã cho
nhap = input("Enter key:value pairs for Dictionary separated by commas (e.g. a:1,b:2): ")
dictionary = {}
for cap in nhap.split(","):
    key, value = cap.strip().split(":")
    dictionary[key.strip()] = value.strip()

print("Original Dictionary:", dictionary)

key_xoa = input("Enter key to delete: ")
if key_xoa in dictionary:
    del dictionary[key_xoa]
    print("Dictionary after deleting key '{}':".format(key_xoa), dictionary)
else:
    print("Key '{}' not found in Dictionary.".format(key_xoa))
