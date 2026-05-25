n = int(input())
is_beautiful = False

while not is_beautiful:
    n+=1
    if len(set(str(n)))==4:
        is_beautiful= True

print(n)