n = int(input())
s = list(map(int, input().split()))

for x in s:
    tp = False
    if x<=3:
        print("NO")
        continue
    else:
        y = x**0.5
        z = round(y)
        if x == z*z:
            if z < 2:
                print("NO")
                continue
            elif z < 4:
                print("YES")
                continue

            if z % 2 == 0 or z % 3 == 0:
                print("NO")
                continue
            
            i=5
            tp = True
            while i**2<=z:
                if z%i==0 or z%(i+2)==0:
                    tp = False
                    break
                i+=6

            print("YES" if tp else "NO")
        else:
            print("NO")

    