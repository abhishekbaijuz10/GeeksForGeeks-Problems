import random

maxlen = int(input("Enter the length of the password"))

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
low_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z']
up_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
           'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
           'Z']

symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<', '&', ';']

all_together = digits + low_case + up_case + symbols

# print(all_together)

r_digits = random.choice(digits)
r_low_case = random.choice(low_case)
r_upcase = random.choice(up_case)
r_symbols = random.choice(symbols)

r_together = r_digits + r_low_case + r_upcase + r_symbols

new_list = []

for chr in range(maxlen - 4):
    new_list.append(random.choice(all_together))
string = ''

for ch in new_list:
    string += ch

print()
print("Password is", string+r_together)

