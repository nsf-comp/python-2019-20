"""
NSF - CODING - Data Structures
"""

dict2 = {
    'studentid' : '100',
    'name': 'Ajay',
    'school' : 'Vidya Mandhir School',
    'city' : 'San Jose'
}

print('1-------------------------')
print(dict2)

dict2['math'] = 98

dict2['science']=92

dict2['geography'] = 87

print('2-------------------------')
print(dict2)



#Update value
dict2['city'] = 'Sunnyvale'
print('3-------------------------')
print(dict2)

"""
Output:
1-------------------------
{
  'studentid': '100', 
  'name': 'Ajay', 
  'school': 'Vidya Mandhir School', 
  'city': 'San Jose'}
2-------------------------
{
   'studentid': '100', 
   'name': 'Ajay', 
   'school': 'Vidya Mandhir School', 
   'city': 'San Jose', 
   'math': 98, 
   'science': 92, 
   'geography': 87
}
3-------------------------
{
   'studentid': '100', 
   'name': 'Ajay', 
   'school': 'Vidya Mandhir School', 
   'city': 'Sunnyvale', 
   'math': 98, 
   'science': 92, 
   'geography': 87
}
"""