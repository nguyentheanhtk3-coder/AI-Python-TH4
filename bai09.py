def dic(x,y):
    for i in x:
        if i not in y:
            y[i] = x[i]
        else:
            y[i] += x[i]
    return y
dic1 = {}
dic2 = {}
while True:
    s = input()
    if s == "":
        break
    key1, value1 = s.split()
    dic1[key1] = int(value1)

while True:
    i = input()
    if i == "":
        break
    key2, value2 = i.split()
    dic2[key2] = int(value2)

print(dic(dic1, dic2))
