"""

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.


"""

#Naive

"""
Iterate through all 3 number tuples that sum to 1000
For each tuple, calculate if a^2 + b^2 = c^2
Calculate abc
"""

import math

def pyTripProd (target):
	bound = math.ceil(target/3)
	
	#target-3
	for c in range (target-3, bound, -1):
		for a in range (1, bound):
			b = target*((target/2)-a)/(target - a)
			if (a**2 + b**2 == c**2):
				print int((a*b*c))
				
				
pyTripProd (1000)