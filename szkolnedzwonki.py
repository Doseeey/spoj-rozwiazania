import sys
msg = sys.stdin.readlines()

def konw(x):
    if len(str(x)) == 1:
        x = "0{}".format(x)
    return x

def prz(a, b):
    res = [a]
    for przerwa in b:
        g, m = map(int, a.split(':'))
        m += 45
        if m > 59:
            g += 1
            m %= 60
        a = '{}:{}'.format(konw(g), konw(m))
        res.append(a)

        g, m = map(int, a.split(':'))
        m += int(przerwa)
        if m > 59:
            g += 1
            m %= 60
        a = '{}:{}'.format(konw(g), konw(m))
        res.append(a)

    g, m = map(int, a.split(':'))
    m += 45
    if m > 59:
        g += 1
        m %= 60
    a = '{}:{}'.format(konw(g), konw(m))
    res.append(a)

    return res


dzwonki = []
start = msg[0][:-1]

for item in msg[1:]:
    dzwonki.append(item[:-1])

output = ''
for g in prz(start, dzwonki):
    if g == prz(start, dzwonki)[-1]:
        output += g
    else:
        output += g
        output += ','

print(output)