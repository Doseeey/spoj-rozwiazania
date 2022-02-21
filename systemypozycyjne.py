def ele(x):
    e = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A']
    res = ''
    while x > 0:
        n = x%11
        res += str(e[n])
        x = x//11
    return res

t = int(input())
while t:
    t -= 1
    n = int(input())
    print(str(hex(n)[2:]).upper(), ele(n)[::-1])