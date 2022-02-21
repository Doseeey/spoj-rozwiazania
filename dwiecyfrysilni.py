def silnia(x):
    res = 1
    for n in range(2, x+1):
        res = res*n
    return res

x = int(input())
while x:
    x -= 1
    num = int(input())

    if num > 9:
        print(0, 0)
        continue

    res = str(silnia(num))
    if len(res) == 1:
        print(0, res)
    else:
        print(res[-2], res[-1])