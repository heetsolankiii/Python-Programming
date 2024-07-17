"""WAP to accept input from the user for radius of circle and display its area and circumference."""

pi = 3.14
radius = int(input("Enter radius: "))
area = pi * radius * radius
circumference = 2 * pi * radius
print("Area of Circle =", area)
print("Circumference of Circle =", round(circumference, 2))