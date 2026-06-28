i1 = list(map(int, input().split()))
tasks = list(map(int, input().split()))

houses = i1[0]
n = i1[1]
current = 1
time = 0

for i in range(n):
    task = tasks[i]
    if current > task:
        time+= houses - current + task
    else:
        time+= task - current
    current = task

print(time)