"""
NSF - CODING - Basic Operators

Membership Operator - 'in'
Evaluates to true if it finds a variable in the specified sequence and false otherwise.
"""
s = 'The membership operators in Python are used to test whether a value is found within a sequence'

print("'value' in '" + s + "'")
print(('value' in s)) #True
print('---------------------------')

print("'Value' in '" + s + "'")
print('Value' in s) #False
print('---------------------------')


print("found within' in '" + s + "'")
print('found within' in s) #True
print('---------------------------')

print("'hello' in '" + s + "'")
print('hello' in s) #False
print('---------------------------')

array = [1,2,5,6,8,10,15,20,35]

print("5 in " + str(array))
print(5 in array) #True

print('---------------------------')

print("100 in " + str(array))
print(100 in array) #False