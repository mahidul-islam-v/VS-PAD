n = int(input())
c = sorted(list(map(int, input().split())))[::-1]
s = sum(c)

x = 0
b = 0

for i in range(n):
    b+= c[i]
    x+= 1
    if b > (s/2):
        break

print(x)