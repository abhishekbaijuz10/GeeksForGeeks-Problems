from itertools import combinations
from itertools import permutations


my_str = input("Enter the string :")
perm = permutations(my_str)
for i in perm:
    print(''.join(i))