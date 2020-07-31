def sum_of_ele(lis, size):
    if size == 0:
        return 0
    else:
        return lis[size - 1] + sum_of_ele(lis, size - 1)


list1 = [11, 5, 17, 18, 23]

total = sum_of_ele(list1, len(list1))

print("Sum of the elements :", total)

# Another method

total2 = sum(list1)
print(total2)