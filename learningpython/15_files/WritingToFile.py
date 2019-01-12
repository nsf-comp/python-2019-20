file = open("mytourlist.txt", "w")

file.write("San Francisco")
file.write("\n")
mylist = ["\t Half Moon Bay \n", "\t 18 miles drive \n", "\t Yosemite National Park \n"]
file.writelines(mylist)

file.write("Grand Canyon\n")
file.write("Miami\n")
file.write("Key West\n")
file.write("Disney, Orlando\n")
file.write("Niagra Falls\n")


file.close()