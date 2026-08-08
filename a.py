import math

n = int(input())

for _ in range(n):
    angle, rad, side = map(float, input().split())
    angle_deg = angle*180/math.pi
    print((math.sin(angle_deg)*side*side/2)-math.pi*rad*rad*angle/360)