t = int(input())
while t:
    t -= 1
    c, k, w = map(int, input().split())
    if c*w > k:
        print('no')
    else:
        print('yes')
