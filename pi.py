PI = 3.14159

# Area of a circle given a radius
def circle():

    radius = input("\nEnter the radius: ")

    radius = float(radius)

    do_math_radius = (radius ** 2)
    area = do_math_radius * PI

    print("Circle: r = ", radius, ", ", "Area = ", area)


# Volume of a sphere given a radius
def sphere():

    radius = input("\nEnter the radius: ")

    radius = float(radius)

    do_math_volume = (4 * PI * (radius ** 3))
    volume = do_math_volume / 3

    print("Sphere: r = ", radius, ", ", "Volume = ", volume)

# Area of a rectangle given a height and width
def rectangle():

    height = float(input("\nEnter the height: "))
    width = float(input("Enter the width: "))

    area = float(height * width)

    print(f"Rectangle: height = {height}, width = {width}, Area = {area}")

# Area of a square given a side length 
def square():
    length = float(input("\nEnter the side length: "))
    
    area = float(length ** 2)

    print(f"Square: side length = {length}, Area = {area}")

# Area of an isosceles triangle given the length of one leg 
# and the height
def isosceles():

    leg = float(input("\Enter the leg length: "))
    height = float(input("Enter the height: "))

    do_math_base = ((leg ** 2 - height ** 2) ** (1/2))
    base = 2 * do_math_base

    area = 1/2 * height * base

    print(f"Isosceles Triangle: side = {leg}, height = {height}, Area = {area}")


# Area of an equilateral triangle given a side length
def equilateral():

    length_equ = float(input("\nEnter the side length: "))

    do_math_area_of_eq = ((3 ** (1/2) / 4))
    area_of_eq = float(do_math_area_of_eq * (length_equ ** 2))

    print(f"Equilateral Triangle: side = {length_equ}, Area = {area_of_eq}")

