s = input()
ss = set()

for c in s:
    if c.isalpha():
        ss.add(c)

print(len(ss))