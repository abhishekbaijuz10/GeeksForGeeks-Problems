from math import pi


def area_circle(r):
    a = pi * (r*r)
    print(a)

r = float(input("Enter the radius of the cicle:"))
area_circle(r)