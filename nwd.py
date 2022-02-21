def nwd(a, b):
    while b:
        a, b = b, a%b
    return a

t = int(input())
liczby = []
while t > 0:
    x = input()
    liczby.append(x)
    t -= 1

for test in liczby:
    x, y = test.split()
    print(nwd(int(x), int(y)))