n = int(input())

odd_sum = 1
prime_sum = 0

def prime_check(param):
	if param == 2 or param == 3:
		return True

	if param % 2==0 or param % 3==0:
		return False

	if (param + 1)/6 %1 == 0 or (param - 1)/6 % 1 == 0:
		if param == 25:
			print(11111)
		return True

odd_count = 0
for i in range(2, 1000):
	if odd_count<n:
		if i%2==1:
			odd_count+= 1
			odd_sum+= i
			
			print(i)
	else:
		break

prime_count = 0
for i in range(2, 1000):
	if prime_count<n:
		if prime_check(i):
			prime_count+= 1
			prime_sum+= i
			
			print(i)
	else:
		break

print(abs(odd_sum-prime_sum))