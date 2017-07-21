"""
Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

#Brute Force

"""
Sum all squares from 1 to 100 and square the sum from 1 to 100 and calculate difference

Runtime: O(n)
"""

def sumSqDiff1 (n):
    sumOfSq = 0
    sum = 0
    for i in range (1, n+1):
        sumOfSquares += i**2
        sum += i
    print ("Difference: ",  sum**2 - sumOfSq)

#Optimization
"""
Series

Falhaber Formula
https://brilliant.org/wiki/sum-of-n-n2-or-n3/

Runtime: O(1)
"""

def arithSeries (n):
    return (n+1)*n/2
	
def sumOfSquares (n):
	return n*(n+1)(2n+1)/6
	
def sumSqDiff2 (n):
	return arithSeries(n)**2 - sumOfSquares(n)