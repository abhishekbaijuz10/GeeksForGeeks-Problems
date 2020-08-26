my_dict = {'abhisek': 2, 'joel': 21, 'mani': 45, 'hairtha': 99}
print(my_dict['mani'])
del my_dict['mani']
print(my_dict)
print(my_dict.pop('abhisek'))
print(my_dict)
new_dict = {x:y for x, y in my_dict.items() if x!= 'joel'}
print(new_dict)