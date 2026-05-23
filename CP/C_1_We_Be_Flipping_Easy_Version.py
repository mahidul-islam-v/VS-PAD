iter = int(input())

for _ in range(iter):
    n = int(input())
    a = list(map(int, input().split()))

    positive_found = False
    positive_end = False

    last_positive = 0

    flip_count = 0
    flip_index = ""

    i = 0

    while i < len(a):
        if a[i] > 0:
            positive_found = True
            last_positive = i

        if positive_found and a[i] < 0:
            positive_end = True

        if positive_end:
            flip_count+= 1
            flip_index+= f"{i} "
            a[:i] = [-x for x in a[:i]]
            i = 0

            positive_found = False
            positive_end = False
        else:
            i+= 1

    print(flip_count)
    print(flip_index)