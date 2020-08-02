def Largest_n_ele(lis, n):
    new_list = []
    for i in range(0, n):
        new_list.append(max(lis))
        lis.remove(max(lis))
    return new_list


my_list = [2, 6, 41, 85, 0, 3, 7, 6, 10]
my_list.sort()
num = int(input("Enter the number of elements :"))
print(Largest_n_ele(my_list, num))
