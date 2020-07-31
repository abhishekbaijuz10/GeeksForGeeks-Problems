import copy
list1 = [1, 2, [3, 5], 4]
list2 = copy.deepcopy(list1)
print("The original elements before deep copy are :")
for i in range(0, len(list1)):
    print(list1[i], end=' ')

print('\r')

list2[2][0] = 7

print("The new list after deep copy are" )
for i in range(0, len(list2)):
    print(list2[i], end=' ')

print('\r')

print("The original elements after deep copying")
for i in range(0, len(list1)):
    print(list1[i], end=" ")

