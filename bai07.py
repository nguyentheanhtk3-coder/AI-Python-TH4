def max_list(l):
    st = set(l)
    n = len(st) - 1
    max_vl = list(st)[n]
    return max_vl

s = input()
mang = [int(x) for x in s.split()]
print(max_list(mang))