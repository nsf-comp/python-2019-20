"""
NSF - CODING - Introduction
Create Date: Oct 17, 2018
"""

#Calculator Program
print("Enter one of the following options:")
print("A - Addition")
print("S - Subtraction")
print("D - Division")
print("M - Multiply")
c = input("Your option: ")
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))

if(c == 'A'):
    a = n1 + n2
    print("Addition: " + str(a))
elif(c =='S'):
    a = n1 - n2
    print("Subtraction: " + str(a))
elif (c == 'D'):
    a = n1 / n2
    print("Division: " + str(a))
elif (c == 'M'):
    a = n1 * n2
    print("Multiply: " + str(a))
else:
    print("Select proper option. ")