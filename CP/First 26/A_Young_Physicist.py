n = int(input())
accx = 0
accy = 0
accz = 0

for _ in range(n):
    vector = [int(x) for x in input().split()]
    accx+= vector[0]
    accy+= vector[1]
    accz+= vector[2]

print("YES" if accx == 0 and accy == 0 and accz == 0 else "NO")