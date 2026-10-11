def st(l):
    dic = {}
    list_new = []
    for i in l:
        if i not in dic:
            list_new.append(i)
            dic[i] = 1     
    return list_new

s = input()
mang = [int(x) for x in s.split()]
print(st(mang))