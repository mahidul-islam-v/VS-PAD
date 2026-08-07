n = int(input())
total = 0

for _ in range(n):
    c, p, q = input().split() 
    p = int(p)
    q = int(q)
    price = p*q
    total+= price + price * (0 if c=="A" else 0.1 if c=="F" else 0.075) + price * 0.05

print(f"{total:.2f}")