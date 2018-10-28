"""
NSF CODE
WEEK 2 HW SUGGESTED ANSWERS
WRITTEN 27 OCT 2018

NOTE: This is a suggested answers. These are not definitive solutions.
"""

grade = input("What grade? ")

if grade >= 90:
    print ("A")
elif grade >= 80:
    # why did I not need to specify grade < 90?
    print ("B")
elif grade >= 70:
    print ("C")
elif grade >= 60:
    print ("D")
else:
    print ("F")