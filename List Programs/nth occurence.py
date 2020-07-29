def remove_the_word(list_, word, n):
    new_list = []
    count = 0
    for j in list_:
        if j == word:
            count += 1
            if count != n:
                new_list.append(j)
        else:
            new_list.append(j)
    lst_ = new_list
    if count == 0:
        print("Item not found ")
    else:
        print("Updated list is :", lst_)

    return new_list


n = int(input("Enter the number of elements in the list :"))
my_list = []
for i in range(0, n):
    element = (input("Enter the words :\n"))
    my_list.append(element)

print(my_list)

word = input("Enter the word to remove :")
number = int(input("Enter the pos of  word :"))

remove_the_word(my_list, word, number)