"""
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

#Unoptimized First Approach

"""
Check divisibility for all numbers up to 20!

Pseudocode

for x from 20 to 20!
    if (x mod 1 == 0 && x mod 2 ... && x mod 20)
        return x
        
Runtime: O(n!) 

Super Slow!
"""

import math

def slowSmallestMultiple (n):
    divisible = True
    for i in range (n,  math.factorial(n), n):
        for j in range (1, n):
            if (i % j != 0):
                divisible = False
                break
        if (divisible): 
            print ("Smallest:", i)
            break
        divisible = True
        
#slowSmallestMultiple (20)

#Optimizations

"""
-For the search, we can skip by 20s, but this does not improve algo by that much; runtime is still O(n!/n)

==Prime Factorization Method==
-We can lower upper limit by prime factorization of all numbers up to 20 and then multiply the maximum number of each prime
found in amongst all numbers 1-20
eg. For n = 5
    2 = 2^1
    3 = 3^1 (max # of 3s)
    4 = 2^2 (max # of 2s)
    5 = 5^1 (max # of 5s)
    Smallest Multiple is 2^2*3*5 = 60

ie. Construct a minimal set of prime factors for which all numbers from 1 to n can be made and multiple them together

Thus iterate through the set of numbers up to 20 and then find the max power of each prime used in any given factorization

This may equate to finding the maximum power a for each prime p <= 20 such that p_i^a_i <= n, need to do proof

Quick Algo for Finding Primes

primes = {2}

for i in range (3, n, 2) #only have to check odd numbers
isPrime = True
for j in range (1, primes.length)
	if i%primes[j] == 0
	isPrime = False
	break
if (isPrime)
	primes.append(i)

GCD/LCM Method

Iteratively calculate the LCM for the product of each number ascending from 1 to n (ie. LCM (1,2), LCM (LCM(1,2),3), etc)

LCM = a*b / GCD (a,b)

GCD: (for a >= b)

GCD (b, a mod b)

"""

def gcd (a, b):
    if (b>a):
        temp = a
        a = b
        b = temp
    if (a % b == 0):
        return b
    else:
        return (gcd (b,  a % b))

def lcm (a, b):
    return (a*b)/gcd(a, b)
    
def smallestMultipleGL (n):
    sm = 1
    for i in range (1,  n):
        sm = lcm(sm, i+1)
    print ("Smallest Multiple: ", int(sm))
    
smallestMultipleGL (20)
