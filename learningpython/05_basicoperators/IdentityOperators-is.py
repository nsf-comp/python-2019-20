"""
NSF - CODING - Basic Operators

Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.
"""

x = 'Program'

y = 'Program'


print(x is y)#True

print(x == y)#True

y = x

print(x is y) #True

z = 'World'

s = 'World '

print(x is z)#False

print(z is s)#False