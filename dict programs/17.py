from collections import Counter


def large_anagran(my_string):
    my_string = my_string.split(' ')

    for i in range(0, len(my_string)):
        my_string[i] = ''.join(sorted(my_string[i]))

    my_string_count = Counter(my_string)

    print(max(my_string_count.values()))


string = 'ant magenta magnate tan gnamate'
large_anagran(string)