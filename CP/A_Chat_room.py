s = input()
result = ""
desired = "hello"

for char in s:
    if result == desired:
        break
    result+= char if char == desired[len(result)] else ""

print("YES" if result==desired else "NO")

