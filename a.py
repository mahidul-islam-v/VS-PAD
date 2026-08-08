n = int(input())

odd_sum = 0
prime_sum = 0

def prime_check(param):
	if param == 2 or param == 3:
		return True

	if param % 2==0 or param % 3==0:
		return False

	for k in range(5, int(param**0.5)+1):
		if (k + 1)/6 %1 == 0 or (k - 1)/6 % 1 == 0:
			if param % k==0:
				return False

	return True

odd_count = 0
for i in range(1, 1000):
	if odd_count<n:
		if i%2==1:
			odd_count+= 1
			odd_sum+= i
	else:
		break

prime_count = 0
for i in range(2, 1000):
	if prime_count<n:
		if prime_check(i):
			prime_count+= 1
			prime_sum+= i
	else:
		break

print(abs(odd_sum-prime_sum))