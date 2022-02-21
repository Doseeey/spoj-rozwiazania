import sys
msg = sys.stdin.readlines()

n = 0
t = '42'
for item in msg:
    i = item[:-1]

    if i == '42' and t != '42':
        n += 1

    t = i
    print(i)

    if n == 3:
        break