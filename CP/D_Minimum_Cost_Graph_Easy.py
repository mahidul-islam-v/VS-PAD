n = int(input())
s = [int(x) for x in input().split()]
t = s[0]
visited = [1]

for i in range(1, n):
    ss = [int(x) for x in input().split()]
    t+= 