n = int(input())
s = list(map(int, input().split()))
r = s.copy()

for i in range(n):
    r[s[i]-1] = i+1


print(*r)