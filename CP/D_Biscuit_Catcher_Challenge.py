n = int(input())
x = [int(x) for x in input().split()]
ans = [0]*n

current = 0
idx = 0

for height in x:
    if height>current:
        idx = x.index(height)
        current = height

    ans[idx]+= 1

print(*ans)