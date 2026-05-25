s = input()

s_unique = set(s)

print("CHAT WITH HER!" if len(s_unique)%2==0 else "IGNORE HIM!")