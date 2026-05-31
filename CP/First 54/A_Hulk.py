n = int(input())

str = ""

for i in range(n):
    if i == 0:
        continue
    str+= "that I love " if i%2==1 else "that I hate "

print(f"I hate {str}it")