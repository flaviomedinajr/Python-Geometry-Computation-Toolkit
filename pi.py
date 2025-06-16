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


def rectangle():

    height = input("\nEnter the height: ")
    width = input("Enter the width: ")

    height = int(height)
    width = int(width)

    area = height * width 
    height = float(height)
    width = float(width)
    area = float(area)

    print(f"Rectangle: height = {height}, width = {width}, Area = {area}")
    