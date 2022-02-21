def stringMerge(a, b):
    res = ''
    for i in range(min(len(a), len(b))):
        res += a[i]
        res += b[i]
    return res

t = int(input())
l = []
while t:
    t -= 1
    x = input()
    l.append(x)

for i in l:
    a, b = map(str, i.split())
    print(stringMerge(a, b))