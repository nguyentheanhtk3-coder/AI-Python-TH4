mang = []
while True:
    s = input()
    if s == "":
        break
    mang.append(s)
def sua_doi(mang):
    for i in range(len(mang)):
        mang[i] = mang[i].title()
    mang_moi = set(mang)
    list_moi = list(mang_moi)
    return list_moi

print(sua_doi(mang))