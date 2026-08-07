n = int(input())
s = [int(x) for x in input().split()]
count = 0


subs = []
for i in range(n):
    subs.append([])

    for j in range(n-i):
        subs[i].append(s)


for sub in subs:
    ans = 0
    for num in sub:
        ans |= num
    if ans%2!=0:
        count+= 1

print(subs)
print(count)