def sprawdz(x1, y1, x2, y2):
    if x1 == 0 or x2 == 0 or y1 == 0 or y2 == 0:
        return "NIE"

    w1 = max(x1, y1)
    w2 = max(x2, y2)
    m1 = min(x1, y1)
    m2 = min(x2, y2)

    if w1 > w2 and m1 > m2:
        return "TAK"
    else:
        return "NIE"


t = int(input())
while t:
    t -= 1
    a, b, c, d = map(int, input().split())
    print(sprawdz(a, b, c, d))