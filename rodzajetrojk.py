def sprawdz(x):

    c = max(x)
    x.remove(c)
    a = x[0]
    b = x[1]

    if c == 0 or a == 0 or b == 0:
        return "brak"
    if c >= a + b:
        return "brak"
    if c*c == a*a + b*b:
        return "prostokatny"
    if c*c < a*a + b*b:
        return "ostrokatny"
    if c*c > a*a + b*b:
        return "rozwartokatny"


import sys
msg = sys.stdin.readlines()

for item in msg:
    x = list(map(float, item.split()))
    print(sprawdz(x))