import sys
msg = sys.stdin.readlines()

def por(a, b, c):
    if b == '==':
        return bool(a == c)
    if b == '!=':
        return bool(a != c)
    if b == '>=':
        return bool(a >= c)
    if b == '<=':
        return bool(a <= c)

for item in msg:
    if item == '':
        continue
    i = item[:-1]
    a, b, c = i.split()
    print(int(por(int(a), b, int(c))))