t = int(input())
iloczyny = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]

def pSuma(x):
    res = 0
    for n in range(len(x)):
        res += int(x[n]) * int(iloczyny[n])
    return res

while t:
    t -= 1
    pesel = input()
    if str(pSuma(pesel))[-1] == '0':
        print("D")
    else:
        print("N")