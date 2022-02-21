def kalk(x):
    res = int(x[0])
    for c, i in enumerate(x):
        if i == '+':
            res += int(x[c+1])
        if i == '-':
            res -= int(x[c+1])
    return res

t = int(input())
while t:
    t -= 1
    dzialanie = input()
    print(kalk(dzialanie))