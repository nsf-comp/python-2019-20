"""
NSF - CODING - Decision Making
"""
I = 10

# 0th indentation level
if(I < 10):
    # 1st indentation level
    print('I less than 10')
    if(I < 2):
        ## 2nd indentation level
        print('I less than 2')
        if(I < 0):
            ## 3rd indentation level
            print('I less than 0')
        elif(I == 1):
            print('I is equal to 1')
        else:
            print('I is greater than 1')
    elif(I == 2):
        print('I equal to 2')
    else:
        print('I greater than 2')
elif(I == 10):
    print('equal to 10')
else:
    print('greater than 10')