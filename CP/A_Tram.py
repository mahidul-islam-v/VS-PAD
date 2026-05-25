n = int(input())
max = 0
passenger = 0

for i in range(n):
    s = list(map(int, input().split()))
    passenger+= s[1]-s[0]
    if passenger > max: max = passenger

print(max)