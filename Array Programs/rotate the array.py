def rotate_by_times(arr, d, n):
    for i in range(d):
        rotate_by_nele(arr, n)


def rotate_by_nele(arr, n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[i + 1] = temp


array = [1, 2, 3, 4, 5, 6, 7, 8]

length = len(array)

element = int(input("Enter the number of elements to rotate"))

rotate_by_times(array, element, length)

print(array)
