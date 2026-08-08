import math

n = int(input())

for _ in range(n):
    angle, rad, side = map(float, input().split())
    print((math.sin(angle)*side**2)-math.pi*rad*rad*angle/360)