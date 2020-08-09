def remove(my_str, i):
    for j in range(len(my_str)):
        if j == i:
            my_str = my_str.replace(m_string[i], '', 1)
    return my_str


m_string = input("Enter the string :")
i = int(input("Enter the index :"))
print(remove(m_string, i))