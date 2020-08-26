from collections import Counter

def bin_angaram_check(num1, num2):
	bin1 = bin(num1)[2:]
	bin2 = bin(num2)[2:]

	zeros = len(bin1)-len(bin2)
	if len(bin2) < len(bin1):
		bin2 = zeros * '0' + bin2
	else:
		bin1 = zeros * '0' + bin1

	dict1 = Counter(bin1)
	dict2 = Counter(bin2)

	if dict1 == dict2:
		print("The 2 binary numbers are Anagrams")
	else:
		print("No")

num1 = 8
num2 = 4
bin_angaram_check(num1, num2)