def dic():
    dic = {}
    while True:
        s = input()
        if s == "":
            break
        key, value = s.split()
        dic[key] = value
    for key, value in dic.items():
        print(f"{key} -> {value}")
    return dic

dic()