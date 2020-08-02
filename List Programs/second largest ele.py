my_list = [x for x in input("Enter the value").split(',')]
print(my_list)

my_list.sort()

my_list.remove(max(my_list))

print(max(my_list))