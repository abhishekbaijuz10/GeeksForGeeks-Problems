def cloning(lst):
    new_list = lst[:]
    return new_list


my_list = [2, 3, 4, 5, 6, 7]
list2 = cloning(my_list)
print("Before cloning", my_list)
print("After cloning ", list2)