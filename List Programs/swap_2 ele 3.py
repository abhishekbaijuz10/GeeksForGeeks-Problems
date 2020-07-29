def swap_positions(list, pos1, pos2):
    get = list[pos1], list[pos2]

    list[pos2], list[pos1] = get

    return list


my_list = [23, 65, 19, 90]

pos1, pos2 = 1, 3

print(swap_positions(my_list, pos1 - 1, pos2 - 1))
