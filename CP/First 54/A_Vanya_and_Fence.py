asd = list(map(int, input().split()))
n = asd[0]
h = asd[1]
s = list(map(int, input().split()))

w = 0

for i in range(n):
    w+= 1 if s[i]<=h else 2

print(w)