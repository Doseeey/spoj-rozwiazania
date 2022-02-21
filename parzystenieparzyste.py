n = int(input())
while n:
    n -= 1
    x = input().split()
    x = x[1:]
    res = []
    for num in range(len(x)):
        if num%2 != 0:
            res.append(x[num])
    for num in range(len(x)):
        if num%2 == 0:
            res.append(x[num])

    print(*res)