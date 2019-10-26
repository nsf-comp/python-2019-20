"""
NSF - CODING - Basic Operators

Membership Operator - 'not in'
Evaluates to true if it does not finds a variable in the specified sequence and false otherwise.

"""
s = 'The membership operators in Python are used to test whether a value is found within a sequence'
print(('value' not in s)) #False

print('Value' not in s)#True

print('found within' not in s)#False

print(('hello' not in s))#True

array = [1,2,5,6,8,10,15,20,35]
print(array)
print("5 in array")
print(5 in array) #True

print("100 in array ")
print(100 in array) #False