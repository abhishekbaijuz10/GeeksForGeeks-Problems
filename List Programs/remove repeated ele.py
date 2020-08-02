def remove_repeated(my_list):
    new_list = []
    for i in range(0, len(my_list)):
        k = i+1
        for j in range(k, len(my_list)):
            if my_list[i] == my_list[j] and my_list[j] not in new_list:
                new_list.append(my_list[i])
    return new_list


list1 = [10, 20, 30, 20, 20, 30, 40,
         50, -20, 60, 60, -20, -20]

print(remove_repeated(list1))