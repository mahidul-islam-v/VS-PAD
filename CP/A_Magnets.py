n = int(input())
streak = 0
c = ""

for i in range(n):
    s = input()
    if c == s[0]: streak= streak+1
    c = s[1]

print(streak+1)

    

    