t = int(input())

for _ in range(t):
    cur = 0
    max_count = 0
    n = int(input())

    for i in range(n):
        c = list(input())
        ones = c.count("1")

        if ones > max_count:
            cur = i+1
            max_count = ones

    print(cur)
