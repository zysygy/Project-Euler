"""
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

# Prime Check

"""
primes = [1,2]
n = 3
isPrime = true
while len(primes) < 10001
	isPrime = true
	for i in primes
		if n mod i = 0 
			isPrime = false
			break
	if (isPrime)
		primes.extend (n)
	n += 1
print primes(len(primes))
"""

import time

def findNthPrime(n):

	start_time = time.time()
	primes = [2]
	num = 3
	isPrime = True
	while len(primes) < n:
		isPrime = True
		for i in primes:
			if num % i == 0:
				isPrime = False
				break
		if (isPrime):
			primes.append(num)
		num += 2
	
	#print (primes[len(primes) - 1])
	#print("--- %s seconds ---" % (time.time() - start_time))
	
findNthPrime (10001)