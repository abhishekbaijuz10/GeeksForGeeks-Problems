def compound_interest(principle, rate, time):
    amount = principle * (pow((1 + rate / 100), time))
    ci = amount - principle
    print("Compound interest is :", ci)


princi = int(input("Enter the principle amount :"))
time = int(input("Enter the time span :"))
rate = float(input("Enter the rate :"))

compound_interest(princi, time, rate)