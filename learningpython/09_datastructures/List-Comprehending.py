"""
NSF - CODING - List - Comprehending

Syntax:
values = [expression for item in collection if condition]

"""

squares = [x * x for x in range(10)]

for no, square in enumerate(squares):
    print(f'{no} --> {square}')

'The following is the cookie cut pattern of adding values to a collection'
print('Cookie Cut pattern')

squares2 = []
for x in range(10):
    squares2.append(x * x)

for no, square in enumerate(squares2):
    print(f'{no} **--> {square}')