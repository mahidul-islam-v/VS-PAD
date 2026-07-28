n = int(input())
s = list(map(int, input().split()))

ans = 0

if s[0]%2 != s[1]%2 or s[0]%2 != s[2]%2 or s[1]%2 != s[2]%2:
    if s[0]%2 == s[1]%2:
        ans = 3
    elif s[0]%2 == s[2]%2:
        ans = 2
    else:
        ans = 1
else:  
    for i in range(len(s)):
        if s[i]%2 != s[i+1]%2:
            ans = i+2
            break

print(ans)

