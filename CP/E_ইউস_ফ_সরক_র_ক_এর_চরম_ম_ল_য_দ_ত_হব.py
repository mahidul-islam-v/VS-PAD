from bisect import bisect_left

n = int(input())
h = [int(x) for x in input().split()]
h.sort()
q = int(input())

for _ in range(q):
    l, s, p = map(int, input().split())
    walls_hit = n - bisect_left(h, l)

    print("Apaa Nai :(" if s-p*walls_hit>0 else "Apaa Ache :)")