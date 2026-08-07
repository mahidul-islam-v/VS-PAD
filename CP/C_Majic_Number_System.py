n = int(input())
x = str(bin(n))[2:]
y = ""

for char in x:
    y+= "7" if char == "1" else "0"

print(y)
