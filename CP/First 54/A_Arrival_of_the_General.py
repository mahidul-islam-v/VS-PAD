n = int(input()) - 1
s = list(map(int, input().split()))
rs = s[::-1]
hi = s.index(max(s))
li = rs.index(min(rs))

tm = hi + li - (1 if hi>(n-li) else 0)

print(tm)