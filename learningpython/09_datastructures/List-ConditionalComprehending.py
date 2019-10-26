"""
NSF - CODING - List - Conditional Comprehending

Syntax:
values = [expression for item in collection if condition]
"""

even_numbers = []

for x in range(20):
    if x % 2 == 0:
        print(x)
        even_numbers.append(x)

