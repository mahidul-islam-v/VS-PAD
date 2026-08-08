import math

gold, years, sons, daughters = map(int, input().split())

for i in range(years):
	gold = gold*0.975

x_factor = sons*2+daughters

print(f"{(gold*2/x_factor):.10f} {(gold/x_factor):.10f}")