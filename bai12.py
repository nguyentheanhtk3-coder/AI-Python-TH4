lic = []
while True:
    s = input().strip()
    if s == "":
        break
    mang = s.split()
    lic.append(mang)

def viet_hoa(x):
    x = x.upper()
    lic_moi = []
    for i in x:
        if i not in lic_moi:
            lic_moi.append(i)
    return lic_moi

print(viet_hoa(lic))