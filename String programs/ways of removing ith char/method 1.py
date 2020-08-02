my_str = 'abhishek'
num = int(input("Enter the index to remove :"))
new_str = ''
for i in range(len(my_str)):
    if i != num:
        new_str = new_str + my_str[i]

print(new_str)