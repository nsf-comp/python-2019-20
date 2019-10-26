"""
NSF - CODING - Data Structures
"""

list2 = [1, 2, True, 40, 'abcd', 'z', 'm', 'n', 'o']
print(list2)

del list2[1]
print(list2)

#prints [1, True, 'abcd', 'z', 'm', 'n', 'o’] — removes 2 from the list

list2.remove('n')
print(list2)

#prints [1, True, 'abcd', 'z', 'm', 'o’]

del list2[2:5]
print(list2)
#prints [1, True, 'm', 'o']

list2.remove(100)
#prints error ValueError: list.remove(x): x not in list
