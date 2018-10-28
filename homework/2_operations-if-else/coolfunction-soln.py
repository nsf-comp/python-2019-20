"""
NSF CODE
WEEK 2 HW SUGGESTED ANSWERS
WRITTEN 27 OCT 2018

NOTE: This is a suggested answers. These are not definitive solutions.
"""

# Get the user's number
number = input("What is your number?")

print("Here's my answer!")

# calculate and print the answer
if number % 2 == 0:
    answer = number + 3
    print(answer)
else:
    answer = number * 4
    print(answer)