def fibonacci_number(num):
    if num < 0:
        print("This is wrong number")
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci_number(num - 1) + fibonacci_number(num - 2)


number = int(input("Enter a number"))
print(fibonacci_number(number))
