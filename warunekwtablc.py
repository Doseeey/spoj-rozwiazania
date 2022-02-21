def war(liczby, warunek):
    res = []
    w, c = warunek.split()
    if w == '>':
        for n in liczby:
            if n > int(c):
                res.append(n)
    elif w == '<':
        for n in liczby:
            if n < int(c):
                res.append(n)
    return res

t = int(input())
nums = []
while t:
    t -= 1
    nums.append(int(input()))
warunek = input()

print(*war(nums, warunek), sep="\n")