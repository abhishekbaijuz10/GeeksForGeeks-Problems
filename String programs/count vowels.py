my_str = 'Hello World'
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
count = 0
for i in my_str:
    if i in vowels:
        count += 1

print(count)