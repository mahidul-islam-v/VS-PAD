s = input().lower()
filtered = ""
vowels = "aeiouy"

for char in s:
    if char not in vowels:
        filtered+= f".{char}"


print(filtered)