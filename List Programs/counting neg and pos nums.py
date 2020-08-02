list1 = [2, -7, 5, -64, -14,-12, 14, 95, 3]
pos_nums = [num for num in list1 if num > 0]
print(pos_nums)
length = len(pos_nums)
length_of_list = len(list1)
print("Positive elements are:", length)
print("The negetive elements are: :", length_of_list - length)