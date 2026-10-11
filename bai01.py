def tong(lit):
    sum = 0
    for i in lit:
        sum += i
    return sum
s = input()
mang = [int(x) for x in s.split()]
print(tong(mang))