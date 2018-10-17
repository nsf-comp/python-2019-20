"""
NSF - CODING - Data Structures
Create Date: Oct 17, 2018
"""
dictionary1 = {
    "name" : 'Karthik',
    "age" : 10,
    "place" : 'Atlanta',
    "email" : 'karthik@gmail.com',
    "school": 'Austin School',
}

print(dictionary1["name"]) #prints Karthik

print(dictionary1.get("place")) #prints Atlanta

#print all the values in the dictionary with the key
for key in dictionary1:
    print("Key: " + key + "  Value: " + str(dictionary1[key]) )
    #Key: name    Value: Karthik
    #Key: age     Value: 10
    #Key: place   Value: Chicago
    #Key: email   Value: karthik @ gmail.com
    #Key: school  Value: Austin elementary school
print("1-----------------------")
for key, value in dictionary1.items():
    print("Key: " + key + "  Value: " + str(value)) #prints key and value
print("2-----------------------")
for value in dictionary1.values():
    print(value)        #print only the values

print("3-----------------------")
print('Prints size / length of dictionary: ' + str(len(dictionary1))) #Prints size / length of dictionary - 5

print("4-----------------------")
if("name" in dictionary1):
    print('name key is present in the dictionary')