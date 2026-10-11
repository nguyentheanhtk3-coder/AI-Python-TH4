def dem(l):
    dic = {}
    for i in l:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    for key, value in dic.items():
        print(f"{key} : {value}")

s = input()
mang = [int(x) for x in s.split()]
dem(mang)