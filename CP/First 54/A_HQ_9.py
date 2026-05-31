s = input()

print("YES" if any(char in "HQ9" for char in s) else "NO")