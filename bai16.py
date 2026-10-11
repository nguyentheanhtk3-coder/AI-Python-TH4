ten_file = input()
dem = 0
with open(ten_file, "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
        dem += 1
print(f"Số dòng: {dem}")