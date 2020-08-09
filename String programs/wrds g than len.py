my_str = input("Enter the string ")
my_str_split = my_str.split()

for i in my_str_split:
    if len(i) > 4:
        print(i)

