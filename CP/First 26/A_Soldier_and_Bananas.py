n = list(map(int, input().split()))
done = False

cost = 0

for i in range(n[2]):
    cost+=n[0]*(i+1)

delta = cost - n[1]

print(delta if delta >= 0 else 0)