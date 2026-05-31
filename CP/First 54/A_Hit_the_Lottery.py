n = int(input())
c = 0
done = False

while not done:
    if n>=200:
        c+= n//100
        n-= c*100
    else:   
        c+=1
        n-= 100 if n%100<n else 20 if n%20<n else 10 if n%10<n else 5 if n%5<n else 1

    if n==0:
        done = True

print(c)