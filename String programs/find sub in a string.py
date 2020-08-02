def check(string1, string2):
    if string1.find(string2) == -1:
        print('no')
    else:
        print("yes")


string = input("Enter the string :")
sub = input("Enter the substring")

check(string, sub)