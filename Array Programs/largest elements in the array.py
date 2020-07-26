lst = []

num = int(input("Enter the size of the array"))
print("Enter the array elements")

for n in range(num):
    numbers = int(input())
    lst.append(numbers)

n = len(lst)

large = lst[0]

for n in range(num):
    if lst[n] > large:
        large = lst[n]

print("The largest element is", large)