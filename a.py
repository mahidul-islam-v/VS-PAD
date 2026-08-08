n = int(input())

for _ in range(n):
	n_apple, queries = map(int, input().split())

	belt = [int(x) for x in input().split()]
	binary_belt = [0]*(n_apple+1)

	for i in range(n_apple):
		binary_belt[i+1]= binary_belt[i]+(1 if belt[i]>=0 else 0)


	for _ in range(queries):
		start, end = map(int, input().split())

		print(binary_belt[end]-binary_belt[start-1])