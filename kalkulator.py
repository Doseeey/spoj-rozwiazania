def calc(a, b, c):
    b = int(b)
    c = int(c)
    if a == '+':
        return b+c
    elif a == '-':
        return b-c
    elif a == '*':
        return b*c
    elif a == '/':
        return b//c
    elif a == '%':
        return b%c

import sys
msg = sys.stdin.readlines()

for item in msg:
    i = item[:-1]
    i = list(i.split())
    print(calc(i[0], i[1], i[2]))