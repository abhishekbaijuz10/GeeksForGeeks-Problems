my_list = [2, 3, 5, 6, 7]
length = len(my_list)
print(my_list)
temp = my_list[0]
my_list[0] = my_list[length - 1]
my_list[length - 1] = temp
print(my_list)
