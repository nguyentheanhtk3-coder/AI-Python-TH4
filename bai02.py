def tuplea(t,x):
    so = t.count(x)
    return so

s = input()
t = tuple(int(x) for x in s.split())
x = int(input())
print(tuplea(t, x))
