def simple_interst(p, t, r):
    print("The principal amount is :", p)
    print("The time period is :", t)
    print("The rate of interest is:", r)

    si = (p * t * r) / 100

    print("The simple interest is :", si)
    return si


simple_interst(8, 6, 8)
