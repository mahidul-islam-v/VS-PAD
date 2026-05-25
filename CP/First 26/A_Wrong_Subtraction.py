n = [int(x) for x in input().split()]
d = n[0]

for i in range(n[1]):
    if d%10==0:
        d//= 10
    else:
        d-= 1

print(d)
