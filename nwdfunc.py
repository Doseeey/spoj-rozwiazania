def nwd(a, b):
    while b:
        a, b = b, a%b
    return a

t = int(input())
while t:
    t -= 1
    n1, n2 = map(int, input().split())
    print(nwd(n1, n2))