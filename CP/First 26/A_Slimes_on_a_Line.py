import math

iteration = int(input())

for _ in range(iteration):
    n = int(input())
    s = list(map(int, input().split()))

    print(math.ceil((max(s) - min(s))/2))