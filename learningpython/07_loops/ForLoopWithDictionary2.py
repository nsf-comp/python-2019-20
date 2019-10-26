"""
NSF - CODING - For Loop - Dictionary
"""

cars = {
    'Toyota' : "Camry",
    'Toyota' : "Corolla",
    'Honda'  : "Accord",
    'Honda'  : "CRV",
    'Nissan' : "Sentra",
    'BMW'    : 'X1',
    'BMW'    : 'X2',
    'BMW'    : 'X3',
    'BMW'    : 'X4',
    'Audi'   : 'A4',
    'Audi'   : 'S4',
    'Audi'   : 'S6',
    'Audi'   : 'S7'
  }

for brand, model in cars.items():
    print(f'{brand} -> {model}')