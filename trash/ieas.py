from collections import Counter

s = list(input())

counts = Counter(s)
keys = list(counts.keys())
values = list(counts.values())
lent = len(keys)
ans = ""

pallable = True
if (lent%2==1):
    cc = 0
    for i in values :
        if i%2!=0 and cc>0:
            cc+= 1
            pallable = False
            break;
else :
    for i in list(counts.values()) :
        if i%2!=0:
            pallable = False
            break;

if not pallable:
    print("NO SOLUTION")
else :
    if (lent%2==1):
        for i in range(lent) :
            for k in range(int(values[i]//2)):
                ans+= keys[i]

        for i in range(lent) :
                    for k in range(int(values[i-i-1]/2)+1):
                        ans+= keys[lent-i-1]

        print(ans)


    


print(keys, values)