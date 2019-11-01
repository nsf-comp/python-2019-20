"""NSF - CODE """

#Calling a Function with in Function

def sumOfTwoNumbers(a,b):
    sum = a+b
    return 'The sum of {} and {} is {}.'.format(a, b, sum)

def main():
    print(sumOfTwoNumbers(2, 3))
    print(sumOfTwoNumbers(123456789, 987654321))
    x=int(input("enter an integer: "))
    y=int(input("enter another integer: "))
    print(sumOfTwoNumbers(x, y))

main()



""" OUTPUT """

The sum of 2 and 3 is 5.
The sum of 123456789 and 987654321 is 1111111110.
enter an integer: 5
enter another integer: 8
The sum of 5 and 8 is 13.
