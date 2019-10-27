"""
NSF - CODING - List - Slicing

Syntax:
list = [start:end:step]

This example demonstrates slicing of the collections to a smaller subset
"""

mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


#Variation 1: both start and end index is set in the slicing
odd_numbers = mylist[0:10:2]

print(odd_numbers)
#prints [1, 3, 5, 7, 9]

#Variation 2: the end index is not provided, hence the function takes till end

odd_numbers2 = mylist[0::2]
print(odd_numbers2)
#prints [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


#Variation 3: the step size is left out and its defaults to one
subset = mylist[2:8]
print(subset)
#prints [3, 4, 5, 6, 7, 8]

#Variation 4: both start and end index are left out and
stride = mylist[::2]
print(stride)
#prints [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

#Variation: Reversing the list
reversedlist = mylist[::-1]
print(reversedlist)
#prints [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


#Reversing the list using reversed function will not modify the original list.
#Here mylist reverse order is stored in revList and myList order doesn't change the order
revList = list(reversed(mylist))
print(revList)

#in reverse() function, it changes the order in the original list
print('------ Before reversing - myList------')
print(mylist)
mylist.reverse()
print('------ After reversing - myList ------')
print(mylist)