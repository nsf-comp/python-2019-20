"""
NSF - CODING - Numbers
Create Date: Oct 17, 2018
"""

import random

print(random.random())

#Prints a random number between 0 and 1. Example: 0.19871922793463193

print(random.randint(1,100))

#Prints a random number between 1 and 100.


items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.sample(items,1))

#picks a random from the list of given numbers and returns a single array

print(random.sample(items,3))

#picks three random numbers from the list of given 10 numbers and returns array of 3 numbers


items = ['Ajay', 'Arti', 'Bala', 'Bhavya','Srijit', 'Karthik', 'Shruti']
print(random.sample(items,2))

#Picks two names at random from the given list of names




items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(items)
#prints [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

random.shuffle(items)
print(items)

#prints [10, 7, 3, 1, 9, 6, 4, 5, 2, 8] -- When you print, the number order may be different.