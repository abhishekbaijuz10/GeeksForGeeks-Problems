import math

def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x


def isfibonacci(n):
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)


for i in range(1, 100):
    if (isfibonacci(i)):
        print(i, "is a fibonacci number")
    else:
        print(i, 'is not a fibonacci series')