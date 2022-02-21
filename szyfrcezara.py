import sys
msg = sys.stdin.readlines()

for item in msg:
    i = item[:-1]
    print(i.translate(str.maketrans(" ABCDEFGHIJKLMNOPQRSTUVWXYZ", " DEFGHIJKLMNOPQRSTUVWXYZABC")))