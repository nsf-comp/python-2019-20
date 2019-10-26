"""
NSF - CODING - For Loop - Enumerate
"""

birds = ['Parrot', 'Golden-crowned Kinglet', 'Acorn Woodpecker', 'Flycatcher', 'Hummingbird', 'Black Duck','Flamingo']
print('Size of the array: ', len(birds))
print('Range of the array: ', range (len(birds)))

for i, bird in enumerate(birds):
    print(f'{i}: {bird}')