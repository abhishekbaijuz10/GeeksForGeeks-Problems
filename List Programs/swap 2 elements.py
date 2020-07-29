def swap_values(list_, a, b):
    temp = list_[a]
    list_[a] = list_[b]
    list_[b] = temp


n = int(input("Enter the number of elements in the list :"))
my_list = []
for i in range(0, n):
    element = int(input("Enter the element :"))
    my_list.append(element)

print(my_list)

first = int(input("Enter the first position"))
second = int(input("Enter the second position"))

swap_values(my_list, first, second)

print(my_list)