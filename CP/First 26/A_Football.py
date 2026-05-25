s = input()
straights = 0
dangerous = False

for i in range(len(s)-1):
    straights = straights+1 if s[i]==s[i+1] else 0

    if straights==6: 
        dangerous = True
        break

print("YES" if dangerous else "NO")