my_list = [x for x in input("Enter the value: ").split('.')]
print(my_list)

first = my_list[0]

for j in my_list:
    if j > first:
        first = j


print("The largest value is :", first)