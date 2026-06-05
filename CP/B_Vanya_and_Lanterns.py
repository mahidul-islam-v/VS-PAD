i1= list(map(int, input().split()))
s = sorted(list(map(int, input().split())))

n= i1[0]
l= i1[1]

rad= 0

for x in s:
    i = s.index(x)
    a = 0 if i==0 else s[i-1]
    b = l if i==len(s)-1 else s[i+1]

    a_dis = x-a
    b_dis = b-x
    new_rad = max(a_dis/2 if i!=0 else a_dis, b_dis/2 if i!=len(s)-1 else b_dis)
    rad = max(rad, new_rad)
    
print(f"{rad:.10f}")