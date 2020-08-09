key_value = {}

key_value[2] = 56
key_value[1] = 2
key_value[5] = 12
key_value[4] = 24
key_value[6] = 18
key_value[3] = 323

print(key_value)

for i in sorted(key_value.keys()):
    print(i, end = ' ')