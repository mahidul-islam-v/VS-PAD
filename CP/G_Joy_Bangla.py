import math

n = int(input())

for _ in range(n):
    t = int(input())
    max_rad = 0
    for i in range(t):
        s = [int(x) for x in input().split()]
        i1 = s[0]
        i2 = s[1]

        max_rad = max(max_rad, math.sqrt(i1*i1+i2*i2))

    print(f"{(math.pi * max_rad* 2):.6f}")