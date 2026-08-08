n = int(input())

for _ in range(n):
	n_apple, queries = map(int, input().split())

	belt = [int(x) for x in input().split()]
	binary_belt = []

	for item in belt:
		binary_belt.append(1 if item>=0 else 0)
			

	for _ in range(queries):
		start, end = map(int, input().split())

		print(sum(binary_belt[start-1:end]))