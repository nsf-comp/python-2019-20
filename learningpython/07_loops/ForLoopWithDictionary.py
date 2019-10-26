"""
NSF - CODING - For Loop - Dictionary
"""

myclass = {
   'Ajay'  : 'ajay@gmail.com',
   'Aarav' : 'aarav@aol.com',
   'Aditi' : 'aditi@yahoo.com'
  }

for name, score in myclass.items():
    print(f'{name} -> {score}')