from collections import Counter

votes = ['john','johnny','jackie','johnny','john','jackie','jamie','jamie', 
'john','johnny','jamie','johnny','john'] 

count_votes = Counter(votes)

dicti = {}

for val in count_votes.values():
	dicti[val] = []

for key, value in votes.items():
	dicti[val].append(key)

maxvote = sorted(dicti.keys(), reverse = True)[0]

if len(dicti[maxvote]) > 1:
	print(sorted(dicti[maxvote]))