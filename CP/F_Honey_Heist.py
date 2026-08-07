n = int(input())

before = set([int(x) for x in input().split()])
after = set([int(x) for x in input().split()])

ans = list(before - after)

print(*reversed(sorted(ans)))