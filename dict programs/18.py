my_str = 'Python is great and Java is also great'

my_str = my_str.split(' ')

new_str = []

for i in range(0, len(my_str)):
    if my_str[i] not in new_str:
        new_str.append(my_str[i])

print(new_str)

