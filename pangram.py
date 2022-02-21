alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word = list(input())
result = []

def all_same(items):
    return all(x == items[0] for x in items)

if sorted(set(word)) == sorted(alp):
    for x in range(len(alp)):
        num = word.count(alp[x])
        result.append(num)
    if all_same(result):
        print("PANGRAM PERFEKCYJNY")
    else:
        print("PANGRAM")
elif sorted(set(word)) != sorted(alp):
    print("NIE")