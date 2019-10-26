"""
NSF - CODING - Functions
"""

from AdditionCalculator import adder as sum
from NoReturnFunction import doSomething


print(sum(10,20))

val = doSomething("Hello Non return function...")
print("Returned value: " + str(val))

