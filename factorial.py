def factorial(n):
    if n < 0:
        return 0
    elif n == 1 or n == 0:
        return 1
    else:
        fact = 1
        while n > 1:
            fact *= n
            n -= 1
        return fact


num = 5
print("Factorial is ", num, "is", factorial(num))