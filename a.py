n = int(input())

for _ in range(n):
	n_apple, queries = map(int, input().split())

	belt = [int(x) for x in input().split()]
	binary_belt = [0]*(n_apple)
	binary_belt[0] = 1 if belt[0]>=0 else 0

	for i in range(1,n_apple):
		binary_belt[i]= binary_belt[i-1]+(1 if belt[i-1]>=0 else 0)

	print(binary_belt)

	for _ in range(queries):
		start, end = map(int, input().split())

		print(binary_belt[end-1]-binary_belt[start-1])