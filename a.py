n = int(input())

odd_sum = 1
prime_sum = 0

def prime_check(param):
	if param == 2 or param == 3:
		return True

	if param % 2==0 or param % 3==0:
		return False

	if (param + 1)/6 %1 == 0 or (param - 1)/6 % 1 == 0:
		return True


for i in range(2, n+1):
	if i%2==1:
		odd_sum+= i

	if prime_check(i):
		prime_sum+= i

print()