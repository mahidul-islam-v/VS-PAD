n = int(input())

for _ in range(n):
	n_apple, queries = map(int, input().split())

	belt = [int(x) for x in input().split()]
	binary_belt = [0]*(n_apple+1)

	for i in range(n_apple):
		binary_belt[i]

	for _ in range(queries):
		start, end = map(int, input().split())

		print(sum(binary_belt[start-1:end]))