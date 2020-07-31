def cloning(lst):
    list_copy = []
    list_copy.extend(lst)
    return list_copy


my_list = [2, 3, 00, 5, 6, 7]
list2 = cloning(my_list)
print(my_list)
print(list2)