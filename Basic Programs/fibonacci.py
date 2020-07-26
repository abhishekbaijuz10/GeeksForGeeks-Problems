def fibonacci(num):
    n1, n2 = 0, 1
    count = 0
    if num < 0:
        print("Wrong Input")
    elif num == 1:
        print(n1)
    else:
        print("Fibonacci terms are:")
        while count < nterms:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1


nterms = int(input("Enter the number"))
fibonacci(nterms)