file = open("quotes.txt", "r")



#print(file.read())

#print(file.readline()) #Reads fist line

#print(file.readline()) #Reads second line

lines = file.readlines() #Reads each line in file and return it as an list
#print(lines)
for line in lines:
    print(line)

#for line in file:
#    print(line)

file.close()
