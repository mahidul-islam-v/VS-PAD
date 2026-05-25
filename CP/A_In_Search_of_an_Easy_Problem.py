n = int(input())
s = list(map(int, input().split()))
is_hard = False

for i in s:
    if i == 1:
        is_hard = True
        break

print("HARD" if is_hard else "EASY")