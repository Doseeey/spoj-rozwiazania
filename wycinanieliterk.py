import sys
msg = sys.stdin.readlines()

def wytnij(c, txt):
    res = ''
    for let in txt:
        if let != c:
            res += let
    return res


for item in msg:
    c, txt = item.split()
    print(wytnij(c, txt))