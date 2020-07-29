def find_the_multi(arr, lens, n):
    mul = 1
    for i in range(lens):
        mul *= (arr[i])
    return mul % n


arr = [100, 10, 5, 25, 35, 14]
n = 11
length = len(arr)
print(find_the_multi(arr, length, n))


