"""
NSF - CODING - List - Conditional Comprehending

Syntax:
values = [expression for item in collection if condition]
"""
'Example without using comprehension feature '
even_numbers = []

for x in range(20):
    if x % 2 == 0:
        print(x)
        even_numbers.append(x)
print('-------------------------')

'Example using comprehension feature'
odd_numbers = [x for x in range(10)
                    if x %2 != 0]

for o in odd_numbers:
    print(o)