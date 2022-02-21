from math import pi

t = int(input())

def cuts(x):
    t = 0
    res = 0
    while t < x:
        t += 2
        res += 1
    return res

def portion(x, y):
    x = x/2
    obw = 2*x*pi
    return round(obw/y, 3)

while t:
    t -= 1
    d, n = map(float, input().split())
    print(portion(d, n), cuts(n))