#bio data print
name =(input("enter your name: "))
age =(input("enter your age: "))
#area of circle
radius = float(input("enter radius of circle: "))
import math
def area(radius):
    return math.pi * radius ** 2
print(f"Hello ",name +"your age is ", age)
print(f"The area of the circle with radius {radius} is {area(radius)}")