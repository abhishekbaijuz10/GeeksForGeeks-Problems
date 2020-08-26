from collections import Counter

string = 'xyyz'
c_string = Counter(string)

same = list(set(c_string.values()))
print(same)
# if len(same) > 2:
#     print("No")
# elif len(same) == 2 and same[1]