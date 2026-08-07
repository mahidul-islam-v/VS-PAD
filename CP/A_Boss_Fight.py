from collections import Counter

n = int(input())

for _ in range(n):
    x = int(input())
    s = [int(x) for x in input().split()]
    count = Counter(s)
    count_keys = list(count.keys())
    count_values = list(count.values())

    count_keys.sort(key=lambda number: count[number])
    count_values.sort()

    damage = 0

    for value in count_values:
        if value<=3:
            damage+= count_keys[count_values.index(value)]*value
        else:
            damage+= count_keys[count_values.index(value)]*

    print(damage)