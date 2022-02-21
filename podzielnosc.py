def podzielnosc(n, x, y):
    res = []
    for i in range(1, n):
        if i % x == 0 and i % y != 0:
            res.append(i)
    return res

t = int(input())
while t:
    t -= 1
    z = input().split()
    print(*podzielnosc(int(z[0]), int(z[1]), int(z[2])))