import sys
msg = sys.stdin.readlines()

def zlicz(text, char):
  count = 0
  for w in text:
      for c in w:
        if ord(c) == char:
          count += 1
  return count


for let in range(256):
    res = zlicz(msg, let)
    if res > 0:
        print(let, res)
