"""
NSF - CODING - For Loop
"""

i = 0
n = 10

while i < n:
    print('before continue statement - ' + str(i))
    i += 1
    if(i < 8): continue
    print('after continue statement')

"""
Output:

before continue statement - 0
before continue statement - 1
before continue statement - 2
before continue statement - 3
before continue statement - 4
before continue statement - 5
before continue statement - 6
before continue statement - 7
after continue statement
before continue statement - 8
after continue statement
before continue statement - 9
after continue statement
"""