import math

n = int(input())
s = list(map(int, input().split()))
one = s.count(1)
two = s.count(2)
three = s.count(3)
four = s.count(4)

cars = four + three + two//2
extra_ones = max(0, one - three)

if two%2!=0:
    cars+= 1
    extra_ones = max(0, extra_ones - 2)

cars+= math.ceil(extra_ones/4)

print(cars)

