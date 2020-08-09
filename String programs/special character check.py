import re


def run(string):
    result = re.compile('[@_!#$%^&*()<>?/|}{~:]')
    if result.search(string) is None:
        print("String is not Accepted")
    else:
        print("String is Accepted")


my_string = input("Enter the string")
run(my_string)
