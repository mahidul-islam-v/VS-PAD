import math
n = list(map(int, input().split(" ")))

area = n[0] * n[1]

results = math.floor(area/2)

print(results)