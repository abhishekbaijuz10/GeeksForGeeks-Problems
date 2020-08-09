def rotate_string(string, number):
    left_first = string[:number]
    left_second = string[number:]
    right_first = string[:len(string) -number]
    right_second = string[len(string) -number:]
    print("Rotated to left :", left_second+left_first)
    print("Rotated to right :", right_second+right_first)



my_string = input("Enter the string :")
num = int(input("Enter the position :"))
rotate_string(my_string, num)