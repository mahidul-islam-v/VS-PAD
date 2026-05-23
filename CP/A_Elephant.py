n = int(input())
s = 0
reached = False

while not reached:
    s+=1
    if n<=5:
        reached = True
    else:
        n = n-5

print(s)