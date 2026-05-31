n1 = input()
n2 = input()
r = ""

for i in range(len(n1)):
    r+= "0" if n1[i]==n2[i] else "1"

print(r)