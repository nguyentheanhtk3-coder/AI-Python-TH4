def vitri(l):
    dic = {}
    for i in range(len(l)):
        if l[i] not in dic:
            dic[l[i]] = str(i);     
        else:
            dic[l[i]] += ", " + str(i);
    for key, value in dic.items():
        print(f"{key} : {value}")

s = input()
mang = [int(x) for x in s.split()]
vitri(mang)