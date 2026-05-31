s = []
hit = set()

for i in range(5):
    s.append(int(input()))


def hit_add(y):
    global c
    for i in range(s[4]//y):
        hit.add(y*(i+1))

for i in range(4):
    hit_add(s[i])

print(len(hit))