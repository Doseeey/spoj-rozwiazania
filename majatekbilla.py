def majatek(a, b, c):
    while b:
        b -= 1
        a *= a
    return a%c

while True:
    u, s, d = map(int, input().split())
    if u == 0 and s == 0 and d == 0:
        break
    print(majatek(u,s,d))