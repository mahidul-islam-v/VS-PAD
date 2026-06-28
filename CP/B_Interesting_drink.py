import bisect

shops = int(input())
prices = sorted(list(map(int, input().split())))
n = int(input())

for i in range(n):
    wallet = int(input())
    drinks = bisect.bisect_right(prices, wallet)
    print(drinks)
