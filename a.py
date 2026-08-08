n = int(input())

for _ in range(n):
	n_apple, queries = map(int, input().split())

	belt = [int(x) for x in input().split()]

	for _ in range(queries):
		start, end = map(int, input().split())

		positive = 0

		for i in range(start-1, end-1):
			if belt[i]>= 0:
				positive+= 1

		print(positive)