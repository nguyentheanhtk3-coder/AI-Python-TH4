def kt(l, x):
    if x in l:
        return True
    else:
        return False

s = input()
l = [int(x) for x in s.split()] 
x = int(input())
print(kt(l, x))