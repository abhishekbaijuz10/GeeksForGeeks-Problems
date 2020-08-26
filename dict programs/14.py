def allAnagram(my_string):
    dict = {}

    for strval in my_string:

        key = ''.join(sorted(strval))

        if key in dict.keys():
            dict[key].append(strval)
        else:
            dict[key] = []
            dict[key].append(strval)