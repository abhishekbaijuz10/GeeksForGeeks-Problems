def split_array(arr, n, k):
    b = a[:k]
    return (a[k::] + b[b::])


arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = 2
arr = split_array(arr, n, position)
for i in range(0, n):
    print(arr[i], end=' ')