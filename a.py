import math

n, limit, rate = map(int, input().split())

trucks = math.ceil(n/limit)

print(trucks, trucks*rate)