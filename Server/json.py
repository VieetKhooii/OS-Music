import json

# Danh sách lưu trữ tên file
filenames = ["file1.json", "file2.json", "file3.json"]

# Danh sách lưu trữ dữ liệu
data = []

# Duyệt qua từng file
for filename in filenames:
    # Đọc dữ liệu từ file
    data.extend(json.load(open(filename)))

# Ghi danh sách kết quả ra file JSON mới
json.dump(data, open("file_ketqua.json", "w"))