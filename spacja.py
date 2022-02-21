def zmiana(x):
    x[0] = str(x[0]).capitalize()
    for i in range(x.count(' ')):
        ind = x.index(' ')
        if ind+1 < len(x):
            x[ind+1] = str(x[ind+1]).capitalize()
        x.remove(' ')
    return x

import sys
msg = sys.stdin.readlines()

for item in msg:
    i = item[:-1]
    res = ''
    print(res.join(zmiana(list(i))))