my_list = [10, 20, 30, 40, 50]
new_list = [sum(my_list[0:x:1]) for x in range(0, len(my_list)+1)]
print(new_list[1:])