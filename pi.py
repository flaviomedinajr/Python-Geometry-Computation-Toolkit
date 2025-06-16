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

    height = int(input("\nEnter the height: "))
    width = int(input("Enter the width: "))

    area = height * width 
    height = float(height)
    width = float(width)
    area = float(area)

    print(f"Rectangle: height = {height}, width = {width}, Area = {area}")

# Area of a square given a side length 
def square():
    length = int(input("\nEnter the side length: "))
    
    area = length ** 2

    area = float(area)
    length = float(length)

    print(f"Square: side length = {length}, Area = {area}")

