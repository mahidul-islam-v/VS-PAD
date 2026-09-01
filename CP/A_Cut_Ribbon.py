n, a, b, c = map(int, input().split())

max = 0

for i in range((n//a)+1):
    for j in range((n//b)+1):
        used = i*a + j*b
        rem = n-used
        if rem>=0 and rem%c==0:
            count = i+j+rem//c
            if count>max: max = count


print(max)