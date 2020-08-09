from collections import Counter

my_string = 'geeksforgeeks'
counter = Counter(my_string)
print(counter)
j = 0
for value in counter.values():
	j += 1
	if value > 1:
		print(list(counter.keys())[j])