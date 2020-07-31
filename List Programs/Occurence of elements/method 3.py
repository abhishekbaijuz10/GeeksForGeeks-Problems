from collections import Counter

l = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

x = 3

d = Counter(l)

print(d)

print('{} has occured  {} times'.format(x, d[x]))