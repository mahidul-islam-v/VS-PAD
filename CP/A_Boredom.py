n = int(input())

for i in range(1, n+1):
    fact = 1
    for j in range(1, i+1):
        fact*=j
    print(fact)

# s = str(fact)
# z_count = 0
# for i in range(len(s)):
#     if s[-(i+1)] == "0":
#         z_count+= 1
#     else:
#         break
