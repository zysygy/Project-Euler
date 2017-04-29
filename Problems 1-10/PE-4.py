"""
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

#First Attempt

"""
Pseudocode

max = 0
For each i from 999 to 100
    For each j from i-1 to 100 #consider edge case of when i = 100
        if (i*j > max)
            stringifiedProd = str(i*j)
            stringifiedProdRev= stringifiedProd[::-1]
            if stringifiedProd == stringifiedProdRev
                max = i*j
        elif break (since we are descending, no palindromes can be bigger than currently found max if max >= i*j for current i)
return max
"""
def palindrome ():
    maxPali = 0
    stringifiedProduct = ""
    stringifiedRev = ""
    for i in range (999, 100,  -1):
        for j in range (i-1,  100,  -1):
            if (i*j > maxPali):
                stringifiedProduct = str(i*j)
                stringifiedRev = stringifiedProduct[::-1]
                if (stringifiedProduct == stringifiedRev):
                    maxPali = i*j
            else: break
    print ("Pali is:", maxPali)
    
palindrome()
