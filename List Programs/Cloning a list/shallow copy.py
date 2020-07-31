import copy

list1 = [1, 2, [3, 5], 4]

list2 = copy.copy(list1)

print(list1)
print(list2)

list2[2][0] = 77

print(list1)
print(list2)
