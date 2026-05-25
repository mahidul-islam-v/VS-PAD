import math

n = list(map(int, input().split(" ")))
sh = n[0]
sw = n[1]
ts = n[2]

thtl = math.ceil(sh/ts)
twtl = math.ceil(sw/ts)

tiles_needed = twtl*thtl

print(tiles_needed)