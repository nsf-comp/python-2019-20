"""
NSF - CODING - Data Structures
Create Date: Oct 17, 2018
"""

set2 = {1,2,3,4,5}
print(set2)

set2.add(7)

print(set2)

# set2.add(7,8)
# This will throw an error. You can add only one element to set

set3 = {7,8,9}

set2 = set2.union(set3)
print(set2)

