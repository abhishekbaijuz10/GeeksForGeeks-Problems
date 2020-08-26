from collections import Counter
from collections import OrderedDict


def non_char_check(str, number):
	j = 0
	my_list = []
	sec_list = []
	for i in range(0, len(str)):
		for j in range(i+1, len(str)):
			if str[i] == str[j]:
				my_list.append(str[i])

	sec_list = [n for n in str if n not in my_list]
	print(sec_list)

	if number > len(sec_list):
		print("The kth non repeating char is less")
	else:
		print(sec_list[number-1])


str = input("Enter the string :")
number = int(input("Enter the kth value"))

non_char_check(str, number)
