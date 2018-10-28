"""
NSF CODE
WEEK 2 HW SUGGESTED ANSWERS
WRITTEN 27 OCT 2018

NOTE: This is a suggested answers. These are not definitive solutions.
"""

# take the user input
user_input = raw_input("What letter?")

# if the input is a capital vowel:
if (user_input == 'A') or (user_input == 'E') or \
        (user_input == 'I') or (user_input == 'O') or (user_input == 'U'):
    # the slash on line 13 just says that the if statement doesn't end there, it continues onto the next line.
    print("This is a capital letter AND a vowel!")
# if the input is a lowercase vowel:
elif (user_input == 'a') or (user_input == 'e') or \
        (user_input == 'i') or (user_input == 'o') or (user_input == 'u'):
    print("This is a lowercase letter AND a vowel.")
# if the input is y:
elif (user_input == 'y') or (user_input == 'Y'):
    print("This is the letter y. Sometimes it's a vowel, and sometimes it's a consonant.")
# any other input:
else:
    print("This is either a consonant or you have given me more than one character.")
