tups = [("akash", 10), ("gaurav", 12), ("anand", 14),
     ("suraj", 20), ("akhil", 25), ("ashish", 30)]

sample = dict(tups)

convert = dict(tups)
dictionary = {}
for a, b in tups:
    dictionary.setdefault(a, []).append(b)


print(dictionary)

print(sample)