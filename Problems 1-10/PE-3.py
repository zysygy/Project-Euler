"""
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

#Initial Attempt
"""
Pseudocode:

n = 600851475143
searchUpTo = n
i = 0
factors = []

#Find all factors
while i < searchUpTo
    if n mod i % 0
        factors.push(i)
        factors.push(n/i) #also add check if i = n/i for square root case
        searchUpTo = n/i #lower max search bound as we find factors going up to n/2

sort factors in descending order

#Check for primality
for i in factors
    #similar to finding factors, determine if any numbers up to n/2 divide into i
    if i is prime
        return i

1. Find all factors of n = 600851475143
-Minor Optimization: Can check only odd numbers since n is odd (odd * even = even), generalize to check number is even or odd 
-Method: check #s in ascending order, taking modulo. If modulo = 0, record checked number and corresponding factor
-Interesting idea: as we check each #, if it is a factor, can we decrease upper limit of what numbers need to be checked?
--eg. we find 3 is not a factor of 100, so we also don't need to check numbers 33 or greater. Any factors of 100 
100 that are greater than 33 will already be found by the pairings with the lower factors (eg. 50 is paired with 2)
Is this that useful?
-store all factors in an array

2. For each factor, determine if it is prime
-starting from largest factors, check if it is prime by checking all numbers up to n/2 (similar case to first step). If any are found, 
skip to next number in array
"""

#Most of these attempted optimizations are probably net neutral in performance and just serve to hurt code readability :)

def findFactors (n):

    lowerFactors = []
    upperFactors = []
    i = 2
    step = 1
    #If n is odd, only need to check odd numbers
    if (n % 2 == 1):
        i = 3
        step = 2
    
    n_search = n
    while (i < n_search):
        if (n % i == 0):
            lowerFactors.append(i)
            if (i != int(n/i)):
                upperFactors.append(int(n/i))
            n_search = int(n/i)
        i += step
    #Reverse array
    upperFactors = upperFactors[::-1]
    return (lowerFactors + upperFactors)


def isPrime (n):
    #Similar to finding factors 
    i = 2
    step = 1
    if (n % 2 == 1):
        i = 3
        step = 2
    n_search = n
    while (i < n_search):
        if (n % i == 0):
            return False
        else:
            n_search = int(n/i)
            i += step
    return True
    
def largestPrimeFactor (n):
    factors = findFactors (n)
    for i in reversed(factors):
        if (isPrime (i)):
            print ("Largest Prime Factor:",  i)
            break

largestPrimeFactor (600851475143)

"""
Different approach
Implement Sieve of Erathosthenes up to root(n) and just pick biggest prime

Research:

Quadratic Sieve (good in general case, slower for smaller factors)

Pollard-Rho (good for numbers up to 100 digits long)

Optimization of checking up to n/i is misguided, just check up to root(n)

The algorithm can be improved further by observing that all primes are of the form 6k ± 1,
with the exception of 2 and 3. This is because all integers can be expressed as 
(6k + i) for some integer k and for i = −1, 0, 1, 2, 3, or 4; 2 divides (6k + 0), (6k + 2), (6k + 4); 
and 3 divides (6k + 3). So a more efficient method is to test if n is divisible by 2 or 3, 
then to check through all the numbers of form 6k ± 1
"""
