my_list = [12, 15, 3, 5, 11, 10]
remove_ele = {11, 5}
new_ele = [i for i in my_list if i not in remove_ele]
print(new_ele)