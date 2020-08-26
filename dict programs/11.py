from collections import Counter

ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

ar1 = Counter(ar1)
ar2 = Counter(ar2)
ar3 = Counter(ar3)

result = dict(ar1.items() & ar2.items() & ar3.items())

new_list = []

for key in result.keys():
	new_list.append(key)

print(new_list)