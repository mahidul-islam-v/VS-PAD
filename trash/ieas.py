from collections import Counter

s = list(input())

counts = Counter(s)
keys = list(counts.keys())
values = list(counts.values())
lent = len(keys)
shum = sum(values)
ans = ""

pallable = True
if (shum%2==1):
    cc = 0
    for i in values :
        if i%2!=0:
            if cc>0:
                pallable = False
                break;
            cc+= 1
            
else :
    for i in list(counts.values()) :
        if i%2!=0:
            pallable = False
            break;

if not pallable:
    print("NO SOLUTION")
else :
    if (shum%2==1):
        for i in range(lent-1) :
            for k in range(int(values[i]//2)):
                ans+= keys[i]
        ans+= keys[lent-1]
        for j in range(lent-1) :
            for k in range(int(values[-j-2]/2)):
                ans+= keys[-j-2]

    if (shum%2==0):
            for i in range(lent) :
                for k in range(int(values[i]//2)):
                    ans+= keys[i]
            for j in range(lent) :
                for k in range(int(values[-j-1]/2)):
                    ans+= keys[-j-1]



print(ans)