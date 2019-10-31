""""NSF - CODING"""

#Function to reverse words in a string

def reverseWords(input_str):

    #split words using string split() function
    input_words=input_str.split(" ")

    # reverse words of the list
    # here inputWords[-1::-1], we have three arguments
    # first is -1 that means start from last element
    # second argument is empty that means move to end of list
    # third argument is difference of steps

    input_words = input_words[-1::-1]
    print("After reversing the index ", input_words)

    # now join words with space
    output = ' '.join(input_words)

    return output

input="Python is the best programming Language"
print("Output string after reversing =",reverseWords(input))



""  output  ""

After reversing the index  ['Language', 'programming', 'best', 'the', 'is', 'Python']
Output string after reversing = Language programming best the is Python
