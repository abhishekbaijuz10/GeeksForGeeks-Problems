from collections import Counter

my_string = 'hello'

wc = Counter(my_string)

print(wc)

j = -1

for val in wc.values():
	j = j+1
	if val > 1:
		print(my_string[j])
