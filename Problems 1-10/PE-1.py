"""
Project Euler: Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

#Generic: For numbers n1 and n2, sum all multiples of either n1 or n2 up to max m

#Naïve Brute Force Method
"""
Check if divisible by 3 or 5, sum values

Pseudocode:

sum = 0
for int i to max:
    if i mod 3 % 0 or i mod 5 % 0
    sum += i
print sum 

General case is O(m)
"""
max = 1000

def bruteForce (n1,  n2): 
    sum = 0
    for x in range (0,  max):
        if (x % n1 == 0) or (x % n2 == 0):
            sum += x
    print (sum)
    
#Arithmetic Series Approach
"""
Observe that
3 + 6 + 9 ... + 999 = 3 (1 + 2 ...+ 333)
Use identity: 1 + 2 + 3 ... + n  = n(1+ n)/2

Psuedocode

sum = 0

multiples1 = 3*(arithmetic series up to 1000/3)
multiples2 = 5*(arithmetic series up to 1000/5)
multiples3 = 15*(arithmetic series up to 1000/15)

print multiples1 + multiples2 - multiples3

General Case O(1)
"""

def arithSeries (n):
    return (n+1)*n/2
    
def sumMultiples (n1, n2):
    numFact1 = int((max - 1)/n1)
    numFact2 = int((max - 1)/n2)
    numFact3 = int((max - 1)/(n1*n2))
    
    #Add multiples for both numbers and subtract their least common multiple factors to remove double counting
    print (n1*int(arithSeries(numFact1))+
             n2*int(arithSeries(numFact2)) -
            (n1*n2)*int(arithSeries(numFact3)))

sumMultiples(3, 5)
