my_str = 'abhishek'
num = int(input("Enter the index :"))
new_str = ''.join([my_str[i] for i in range(0, len(my_str)) if i != num])
print(new_str)