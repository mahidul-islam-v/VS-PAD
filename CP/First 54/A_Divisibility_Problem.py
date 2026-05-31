n = int(input())

for i in range(n):
    s = list(map(int, input().split()))
    a = s[0]
    b = s[1]
    print(b-(a%b) if a%b!=0 else 0)