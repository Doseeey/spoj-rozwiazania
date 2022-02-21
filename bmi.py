t = int(input())
imiona = []
wskaznik = []
while t > 0:
    n, m, h = input().split()
    bmi = round(int(m)/(int(h)/100)**2, 1)
    imiona.append(n)
    wskaznik.append(bmi)
    t -= 1

index = 0
print("niedowaga")
for bmi in wskaznik:
    if bmi < 18.5:
        print(imiona[index])
        index += 1
    else:
        index += 1
index = 0
print()
print("wartosc prawidlowa")
for bmi in wskaznik:
    if bmi >= 18.5 and bmi < 25:
        print(imiona[index])
        index += 1
    else:
        index += 1
index = 0
print()
print("nadwaga")
for bmi in wskaznik:
    if bmi >= 25:
        print(imiona[index])
        index += 1
    else:
        index += 1