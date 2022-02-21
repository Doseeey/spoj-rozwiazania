T = [1]
for i in range(1,24):
    T.append(T[i-1]*i)

for lol in range(int(input())):
    index = int(input())
    print(T[index])