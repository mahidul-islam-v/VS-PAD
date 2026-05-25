n = input()
ln_count = 0

for char in n:
    if char in "47":
        ln_count+= 1

print("YES" if ln_count == 4 or ln_count ==7 else "NO")