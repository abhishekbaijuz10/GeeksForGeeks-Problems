main_string = input("Enter the string :")
t = ['0', '1']
count = 0
for i in main_string:
    if i not in t:
        count = 1
        break
    else:
        pass

if count == 1:
    print("not Boolean ")
else:
    print("Boolean")