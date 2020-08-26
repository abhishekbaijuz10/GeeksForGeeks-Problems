from collections import OrderedDict

input = 'engineers rock'
pattern = 'egr'

dict = OrderedDict.fromkeys(input)
ptrlen = 0

for key in dict.items():
	if key == pattern[ptrlen]:
		ptrlen += 1

	if ptrlen == len(pattern):
		print(True)

print(False)