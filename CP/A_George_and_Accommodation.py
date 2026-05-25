n = int(input())
c = 0

for i in range(n):
    s = list(map(int, input().split()))
    c+= 1 if s[0]+1<s[1] else 0

print(c)