t = int(input())
for proba in range(t):
    print(input().translate(str.maketrans(" TUVWXYZABCDEFGHIJKLMNOPQRS" ," ABCDEFGHIJKLMNOPQRSTUVWXYZ")))