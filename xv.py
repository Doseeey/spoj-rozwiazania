def test(x):
    if not x%15:
        return "TAK"
    else:
        return "NIE"

while True:
    t = int(input())
    if t == 0:
        break
    print(test(t))