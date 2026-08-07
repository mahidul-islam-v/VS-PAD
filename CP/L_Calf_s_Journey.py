import math
n = int(input())

for _ in range(n):
    x = int(input())
    s = 0 if x == 0 else 2 if x == 1 else 1 if x == 2 else (math.floor(x/3) + (0 if x%3 == 0 else 1))
    print(s)