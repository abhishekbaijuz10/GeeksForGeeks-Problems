my_str = input("Enter the sentence :")
my_str_spli = my_str.split()
print(my_str_spli)

for i in my_str_spli:
    if len(i) % 2 == 0:
        print(i)


