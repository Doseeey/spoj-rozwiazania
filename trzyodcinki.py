begin = []
end = []
for inp in range(3):
    p, k = input().split()
    begin.append(int(p))
    end.append(int(k))

if max(begin) <= min(end):
    print(max(begin), min(end))
else:
    print("null")