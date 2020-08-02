my_list = [10, 21, 4, 45, 66, 93, 1]
even = 0
odd = 0
num = 0
even = len(list(filter(lambda x: (x % 2) == 0, my_list)))
odd = len(list(filter(lambda x: (x % 2 )!= 0, my_list)))
print(even)
print(odd)