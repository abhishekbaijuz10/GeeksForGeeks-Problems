def prime_number(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(num, "not a prime number")
                print(i, "times", num // i, "is", num)
                break
        else:
            print(num, "is a prime number")
    else:
        print("The number is not a prime number")


number = int(input("Enter the number to check prime :"))
prime_number(number)
