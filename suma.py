import sys
msg = sys.stdin.readlines()
res = 0
for item in msg:
    i = item[:-1]
    res += int(i)
    print(res)