def palindrom(x):
    i = 0
    while str(x) != str(x)[::-1]:
        i += 1
        y = str(x)[::-1]
        x += int(y)
    return x, i

n = int(input())
while n:
    n -= 1
    t = int(input())
    r = palindrom(t)
    print(r[0], r[1])