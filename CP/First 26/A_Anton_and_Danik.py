n = int(input())
s = input()

anton = 0
derek = 0

for char in s:
    if char=="A":
        anton+=1
    else:
        derek+=1

print("Anton" if anton>derek else "Danik" if derek>anton else "Friendship")