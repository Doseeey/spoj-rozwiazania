def nwd(a, b):
    while b:
        a, b = b, a%b
    return a

u1, u2 = input().split()
l1, m1 = map(int, u1.split("/"))
l2, m2 = map(int, u2.split("/"))

licz = l1*m2 + l2*m1
mian = m1*m2

nw = nwd(licz, mian)
lk = int(licz/nw)
mk = int(mian/nw)

print("{}/{} + {}/{} = {}/{}".format(l1, m1, l2, m2, lk, mk))
