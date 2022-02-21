from math import fabs

def avg(x):
    return sum(x) / len(x)

t = int(input())
while t:
    t -= 1
    x = list(map(int, input().split()))
    a = avg(x)
    res = 0
    for n in x:
        if fabs(n - a) < fabs(res - a):
            res = n
    print(res)