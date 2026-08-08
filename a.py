import math

gold, years, sons, daughters = map(int, input().split())

for i in range(years):
	gold = gold*0.975

x_factor = sons*2+daughters

print(gold*2/x_factor, gold/x_factor)