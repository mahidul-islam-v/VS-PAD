n, k = list(map(int, input().split()))


print(k*2-1 if k<=((n+1)//2) else (k-((n+1)//2))*2)