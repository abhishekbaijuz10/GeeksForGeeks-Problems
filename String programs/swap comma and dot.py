my_string = '14, 625, 498.002'
dict1 = {'.': ',', ',': '.'}
t = my_string.maketrans(dict1)
final = my_string.translate(t)
print(final)