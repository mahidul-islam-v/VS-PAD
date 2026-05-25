n = int(input())
s = 0

for _ in range(n):
    i = input()
    can_do = list(map(int, i.split()))
    can_do_count = sum(can_do)

    if can_do_count >= 2:
        s+=1

print(s)