list1 = []
num = int(input("Enter the number of elements in the list"))

for i in range(num):
    ele = int(input("Enter the value :"))
    list1.append(ele)


print(min(list1))