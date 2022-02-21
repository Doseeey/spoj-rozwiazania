def spr(a, b):
    while True:
        a += 1
        if list(str(a)).count('5') == b:
            return a

n, k = input().split()
print(spr(int(n), int(k)))