n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
z = set(x[1:] + y[1:])
z.discard(0)

print("I become the guy." if len(z)==n else "Oh, my keyboard!")