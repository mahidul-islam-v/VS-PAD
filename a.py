import math

gold, years, sons, daughters = map(int, input().split())

for i in range(years):
	gold = gold*0.975

x_factor = sons*2+daughters

s = gold*2/x_factor, gold/x_factor
d = gold/x_factor, gold/x_factor

print(f"{s:.10f}")