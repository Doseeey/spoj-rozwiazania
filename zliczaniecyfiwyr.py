import sys
msg = sys.stdin.readlines()

def zlicz(x):
    n = 0
    s = 0
    for w in x:
        if w.isdigit():
            n += 1
        else:
            s += 1
    return n, s

for item in msg:
    i = item[:-1]
    dane = list(i.split())
    print(*zlicz(dane))