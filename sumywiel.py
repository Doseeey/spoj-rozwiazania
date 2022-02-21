import sys
msg = sys.stdin.readlines()

kRes = 0

for item in msg:
    i = item[:-1]
    dane = list(map(int, i.split()))
    res = 0
    for n in dane:
        res += n
    print(res)
    kRes += res

print(kRes)