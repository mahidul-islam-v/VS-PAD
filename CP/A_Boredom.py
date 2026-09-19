n = int(input())

for _ in range(n):
    [a, b] = [int(x) for x in input().split()]
    print("YES" if (a+b)%3==0 and ((2*a)>=b and ((2*b)>=a)) else "NO")
