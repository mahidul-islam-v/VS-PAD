m = list(map(int, input().split()))
l = m[0]
n = m[1]

os = list(input())
ns = [os[0]]

for x in range(n):
    for i in range(1,l):
        if os[i-1]=="B" and os[i]=="G":
            ns[i-1] = "G"
            ns.append("B")
        else:
            ns.append(os[i])
    os = ns
    ns = os[:1]

print("".join(os))