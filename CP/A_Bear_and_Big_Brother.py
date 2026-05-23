s = list(map(int, input().split()))
limark = s[0]
bob = s[1]
i = 0
is_bigger = False

while not is_bigger:
    limark*=3
    bob*=2
    i+=1

    if limark>bob:
        print(i)
        is_bigger = True
    
