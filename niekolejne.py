def niekolej(x):
    res = []

    if x == 0:
        return [0]

    if x <= 2:
        return ["NIE"]

    if x == 3:
        return [1, 3, 0, 2]

    for i in range(0, x+1,2):
        res.append(i)
    for j in range(1, x+1, 2):
        res.append(j)
    return res

n = int(input())
print(*niekolej(n))