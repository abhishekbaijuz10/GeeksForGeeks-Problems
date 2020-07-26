def square_sum(num):
    sm = 0
    while num != 0:
        sm += (num * num * num)
        num -= 1
    return sm


print(square_sum(5))
