def st(l):
    st = set(l)
    return st

s = input()
mang = [int(x) for x in s.split()]
print(st(mang))