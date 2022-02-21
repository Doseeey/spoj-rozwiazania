k, n = map(int, input().split())
x = input().split()
if n == 0 or n == 1:
    print(*x)
else:
    y = x[-(n-1):]
    y += x[:(k-n+1)]
    print(*y)