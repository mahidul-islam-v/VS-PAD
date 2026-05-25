n = int(input())

for _ in range(n):
    i = input()
    l = len(i)
    word = i
    
    if l > 10:
        word = f"{i[0]}{l-2}{i[l-1]}"

    print(word)