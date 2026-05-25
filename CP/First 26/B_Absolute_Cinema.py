iter = int(input())

for _ in range(iter) :
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # a_max = max(a)
    # max_index = a.index(a_max)

    for i in range(n):
        # if i != max_index:
        if a[i]>b[i]:
            a[i], b[i] = b[i], a[i]
    
    print(max(a)+sum(b))

    