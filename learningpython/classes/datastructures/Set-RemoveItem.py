"""
NSF - CODING - Data Structures
Create Date: Oct 17, 2018
"""

set1 = {1,2,3,4,5,6}
print(set1) #{1, 2, 3, 4, 5, 6}

set1.discard(5)
print(set1) #{1, 2, 3, 4, 6}

set1.remove(2)
print(set1)#{1, 3, 4, 6}

print(set1.pop()) #1

print(set1) #{3, 4, 6}

set1.clear()
print(set1) #set()