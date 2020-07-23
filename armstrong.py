def armstrong(number):
    add = 0
    num = number
    while num > 0:
        digit = num % 10
        add += (digit**3)
        num = num // 10

    if add == arm_num:
        print("The number is a armstrong number")
    else:
        print("The number is not a armstrong number")


arm_num = int(input("Enter the number :"))
armstrong(arm_num)

