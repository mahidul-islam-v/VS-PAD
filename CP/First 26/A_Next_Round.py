def mapString(i):
    return list(map(int, i.split(" ")))

n1 = mapString(input())
s = mapString(input())

n = int(n1[0])
k = int(n1[1])

advances = 0

sn = s[k-1]

for score in s:
    if score >= sn and score>0:
        advances+= 1

print(advances)