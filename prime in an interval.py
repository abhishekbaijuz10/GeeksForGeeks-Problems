def prime_interval(start, stop):
    for val in range(start, stop + 1):
        if val > 1:
            for i in range(2, val):
                if (val % i) == 0:
                    break
            else:
                print(val)


start = int(input("Enter the first number:"))
stop = int(input("Enter the second number :"))

prime_interval(start, stop)