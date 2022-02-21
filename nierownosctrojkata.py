import sys
msg = sys.stdin.readlines()

for item in msg:
    i = item[:-1]
    x = map(float, i.split())
    x = list(x)

    a = max(x)
    b = min(x)

    x.remove(max(x))
    x.remove(min(x))

    c = float(x[0])

    if b + c < a:
        print(0)
    else:
        print(1)