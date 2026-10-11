file = input("Link file: ")
mang = input().split()
with open(file, "a", encoding="utf-8") as f:
    for i in mang:
        f.write(i)
        f.write("\n")

with open(file, "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())