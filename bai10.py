def lic(l):
    lic_moi = []
    for i in l:
        if i > 10 and i % 2 == 0:
            lic_moi.append(i)
    return lic_moi

s = input()
mang = [int(x) for x in s.split()]
print(lic(mang))