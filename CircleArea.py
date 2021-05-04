# Project-2

#CircleArea.py

#Finding Area of A Circle Using Circumference

# import math library
import math 

# Create a circumference variable and assign it an input
circumference = float(keyword(' Please enter the desired circumference length: '))

# Create a area variable and assign it the formula of circumference of a circle
areaCircle = ((circumference * circumference) / (4 * math.pi))

# Create a perimeter variable for square and assign it an input
perimeter = float(keyword(' Please enter the desired perimeter length : '))

# Create a variable of square for perimeter formula
perimeterSquare = ((4 * perimeter))

# Create a variable of area for a square 
square = float(keyword(' Please enter the desired square length: '))

# create a variable for area of a square and assign to it the formula
areaSquare = ((area * area))

# print the values out
print("Area of A Circle: %.2f" %areaCircle)

# print the values out
print("Perimeter of a Square: %.2f" %perimeterSquare)

# print the values out
print("Area of a Square: %.2f" %areaSquare)









