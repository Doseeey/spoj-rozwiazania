x = int(input())
while x:
    x -= 1
    a, b = map(int, input().split())

    if b == 0:
        print(1)
        continue

    loop = b % 4
    a = int(str(a)[-1])


    res = a
    while loop-1:
        loop -= 1
        res *= a
    print(str(res)[-1])