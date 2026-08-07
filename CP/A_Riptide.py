n = int(input())

for _ in range(n):
    arr = list(map(int, input().split()))
    arr.sort()
    a = arr[0]
    b = arr[1]
    c = arr[2]
    print(0 if a==b or a==c or b==c else min(b-a, c-b))