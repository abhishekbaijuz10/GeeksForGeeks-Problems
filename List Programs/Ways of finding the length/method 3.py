from operator import length_hint
my_list = [1, 2, 3, 4, 5, 6]
print(str(my_list))
list_len = len(my_list)
list_len_hint = length_hint(my_list)
print(list_len)
print(list_len_hint)