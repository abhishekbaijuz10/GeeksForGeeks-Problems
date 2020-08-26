from collections import Counter

s1 = 'ABHISHEKsinGH'
s2 = 'gfhfBHkooIHnfndSHEKsiAnG'

counters1 = Counter(s1)
counters2 = Counter(s2)

result = (counters1 & counters2)


if result == Counter(s1):
    print("Possible")
else:
    print("Not possible")