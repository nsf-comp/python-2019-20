"""
NSF - CODING - List - Slicing - Delete elements

Syntax:
list = [start:end:step]

This example demonstrates deleting elements using slicing
"""

mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print('---------- Initial list  ---------- ')

print(mylist)


del mylist[10:]

print('---------- After deleting elements from 10th index    ---------- ')

print(mylist)
