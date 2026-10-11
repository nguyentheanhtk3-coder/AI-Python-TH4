def tb(x):
    diem_tb = sum(x) / len(x)
    return diem_tb

def phan_loai(y):
    if y >= 8.5:
        pl = "Giỏi"
    elif y >= 7:
        pl = "Khá"
    elif y >= 5:
        pl = "Trung bình"
    else:
        pl = "Yếu"
    return pl

danh_sach = {}
while True:
    name = input()
    if name == "" :
        break
    s = input()
    bang_diem = [float(x) for x in s.split()]
    n = tb(bang_diem)
    danh_sach[name] = phan_loai(n)

for x,y in danh_sach.items():
    print(f"{x} : {y}")