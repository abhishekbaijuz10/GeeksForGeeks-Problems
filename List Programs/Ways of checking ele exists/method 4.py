from bisect import bisect_left
my_list = [2, 3, 4, 5, 6, 7]
my_list_bisect = [2, 3, 4, 5, 6, 7]

my_list = set(my_list)
if 4 in my_list:
    print("The element exists")

my_list_bisect.sort()
if bisect_left(my_list_bisect, 10):
    print("The element exists")