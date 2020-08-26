from collections import Counter

my_string = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]

freq = {}
for item in my_string:
        freq[item] = my_string.count(item)

for key, value in freq.items():
    print("%d : %d" % (key, value))

print(my_string.count(1))