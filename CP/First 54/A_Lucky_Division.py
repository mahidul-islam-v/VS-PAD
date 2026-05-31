n = int(input())
lucky = False
luckies = [4,7,44,47,74,77,444,447,474,477,744,747,774,777]

for v in luckies:
    if not lucky and n%v == 0:
        lucky = True
    

print("YES" if lucky else "NO")