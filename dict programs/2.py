import collections

my_dict = collections.defaultdict(lambda: "key is not found")

my_dict['a'] = 1

my_dict['b'] = 2

print(my_dict['a'])

print(my_dict['c'])
