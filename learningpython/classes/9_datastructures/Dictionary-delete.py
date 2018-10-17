"""
NSF - CODING - Data Structures
Create Date: Oct 17, 2018
"""

dictionary1 = {
    "name" : 'Karthik',
    "age" : 10,
    "place" : 'Atlanta',
    "email" : 'karthik@gmail.com'
}


dictionary1["place"] = 'Chicago'  #Changing value

print(dictionary1.get("place")) #prints Chicago

dictionary1["school"]="Austin elementary school"  # Adding new element
print(dictionary1["school"])

dictionary1["something"]= "somethig new" # Adding new element

del dictionary1["something"] #Removes the element from the dictionary list