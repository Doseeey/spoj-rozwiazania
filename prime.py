def test_pierwszej(x):
    if x == 1:
        return False
    if x >= 2:
        for y in range(2, x):
            if not (x % y):
                return False
    return True

n = int(input())
liczby = []
while n > 0:
    n -= 1
    liczby.append(int(input()))

for num in liczby:
    if test_pierwszej(num):
        print("TAK")
    else:
        print("NIE")