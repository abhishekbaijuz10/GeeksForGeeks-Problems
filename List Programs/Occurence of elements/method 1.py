def oc_checking(ls, x):
    count = 0
    for i in ls:
        if i == x:
            count += 1
    return count


lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x, oc_checking(lst, x)))