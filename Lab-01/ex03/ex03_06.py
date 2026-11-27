nhap = input("Nhap cac cap key:value cho Dictionary, cach nhau boi dau phay (vi du: a:1,b:2): ")
dictionary = {}
for cap in nhap.split(","):
    key, value = cap.strip().split(":")
    dictionary[key.strip()] = value.strip()

print("Dictionary ban dau:", dictionary)

key_xoa = input("Nhap key can xoa: ")
if key_xoa in dictionary:
    del dictionary[key_xoa]
    print("Dictionary sau khi xoa:", dictionary)
else:
    print("Khong tim thay key trong Dictionary.")
