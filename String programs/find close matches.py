from difflib import get_close_matches

patterns = ['ape', 'apple', 'peach', 'puppy']
my_str = input("Enter to find")
print(get_close_matches(my_str, patterns, 1))

