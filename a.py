import math

gold, years, sons, daughters = map(int, input().split())

for i in range(years):
	gold = gold*0.975

print(gold)