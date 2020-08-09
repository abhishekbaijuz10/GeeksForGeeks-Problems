my_str = input("Enter the string :")
i = int(input("Enter the index :"))
first = my_str[:i - 1]
second = my_str[i:]
print(first + second)