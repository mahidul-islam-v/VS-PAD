import math

n = int(input())

for _ in range(n):
    m = int(input())
    count = 0
    s = [int(x) for x in input().split()]
    for num in s:
        count+= 1 if math.sqrt(num)%1 != 0 else 0

    print(count)