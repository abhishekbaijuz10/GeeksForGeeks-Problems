original = 'abcdefghijklmnopqrstuvwxyz'
reverse = original[::-1]
dictchars = dict(zip(original, reverse))
print(dictchars)

n = 5
mirror = ''

first = original[0:n]
second = original[n:]

for i in range(0, len(second)):
    mirror = mirror + dictchars[second[i]]

print(first + '' + mirror)
