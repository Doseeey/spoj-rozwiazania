def liniowa(a, b, c):
    if a == b and b != c:
        return "BR"
    if a == 0 and b == 0:
        return "NWR"
    if a == 0 and b == c:
        return "NWR"
    if a == 0 and b != 0:
        return "BR"
    x = (c - b) / a
    if x == 0.0:
        return '0.00'
    return round(x, 2)

a, b, c = map(float, input().split())
print(liniowa(a, b, c))
