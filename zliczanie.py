import sys
msg = sys.stdin.readlines()

def zlicz(a, c):
    res = 0
    for i in c:
        if int(i) == int(a):
            res += 1
    return res

for item in msg:
    i = item[:-1]
    dane = list(i.split())
    a = dane[0]
    c = dane[2:]
    print(zlicz(a, c))
