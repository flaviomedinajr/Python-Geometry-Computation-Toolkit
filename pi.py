# Author: Flavio Medina

PI = 3.14159


# Area of a circle given a radius.
def circle():
    print("\n###-- AREA --###")
    radius = input("\nEnter the radius: ")

    radius = float(radius)

    do_math_radius = (radius ** 2)
    area = do_math_radius * PI

    print(f"\nAnswer:\nCircle: r = {radius}, Area = {area}")


# Volume of a sphere given a radius 
def sphere():
    print("\n###-- SPHERE --###")

    radius = input("\nEnter the radius: ")

    radius = float(radius)

    do_math_volume = (4 * PI * (radius ** 3))
    volume =  do_math_volume / 3

    print(f"\nAnswer:\nSphere: r = {radius}, Volume = {volume}")


# Area of a rectangle given a height and width
def rectangle():
    print("\n###-- RECTANGLE --###")

    height = input("\nEnter the height: ")
    width = input("Enter the width: ")

    height = int(height)
    width = int(width)

    area = height * width 
    height = float(height)
    width = float(width)
    area = float(area)

    print(f"\nAnswer:\nRectangle: Height = {height}, Width = {width}, Area = {area}")


# Area of a square given a side length 
def square():
    print("\n###-- SQUARE --###")
    
    length = input("\nEnter the side length: ")
    
    length = int(length)

    area = length ** 2
    
    print(f"\nAnswer:\nSquare: Side Length = {float(length)}, Area = {float(area)}")


# Area of an isosceles triangle given the length of one leg and the height.
def isosceles():
    print("\n###-- ISOSCELES --###")

    leg = input("\nEnter the leg length: ")
    height = input("Enter the height: ")

    leg = int(leg)
    height = int(height)

    do_math_base = ((leg ** 2 - height ** 2) ** (1 / 2))
    base = 2 * do_math_base 

    area = 1/2 * height * base

    area = float(area)
    leg = float(leg)
    height = float(height)

    print(f"\nAnswer:\nIsosceles Triangle: Leg Length = {leg}, Height = {height}, Area = {area}")


# Area of an equilateral triangle given a side length.
def equilateral():
    print("\n###-- EQUILATERAL --###")

    length_equ = input("\nEnter the side length: ")

    length_equ = int(length_equ)

    do_math_area_of_eq = ((3 ** (1/2) / 4))
    area_of_eq = do_math_area_of_eq * (length_equ ** 2)

    area_of_eq = float(area_of_eq)
    length_equ = float(length_equ)

    print(f"\nAnswer:\nEquilateral Triangle: Side Length = {length_equ}, Area = {area_of_eq}")


# Area of a trapezoid given base 1, base 2, and height
def trapezoid():
    print("\n###-- TRAPEZOID --###")

    base_1 = input("\nEnter base 1: ")
    base_2 = input("Enter base 2: ")
    height = input("Enter height: ")

    base_1 = int(base_1)
    base_2 = int(base_2)
    height = int(height)

    do_math_area_of_trapezoid = 1/2 * (base_1 + base_2)
    area = do_math_area_of_trapezoid * height

    area = float(area)
    base_1 = float(base_1)
    base_2 = float(base_2)
    height = float(height)

    print(f"\nAnswer:\nTrapezoid: Base 1 = {base_1}, Base 2 = {base_2}, Height = {height}, Area = {area}\n")


# Main 
def main():
    while True:
        print("\nChoose a shape to calculate:")
        print("1. Circle")
        print("2. Sphere")
        print("3. Rectangle")
        print("4. Square")
        print("5. Isosceles Triangle")
        print("6. Equilateral Triangle")
        print("7. Trapezoid")
        print("0. Exit")
        choice = input("Enter your choice (0-7): ")

        if choice == "1":
            circle()
        elif choice == "2":
            sphere()
        elif choice == "3":
            rectangle()
        elif choice == "4":
            square()
        elif choice == "5":
            isosceles()
        elif choice == "6":
            equilateral()
        elif choice == "7":
            trapezoid()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()



# Runs all at once through a single main() function
# That is another approached this code
# def main():
#     # For Area - Area of a circle given a radius.

#     radius = input("\nEnter the radius: ")

#     radius = float(radius)

#     do_math_radius = (radius ** 2)
#     area = do_math_radius * PI

#     print(f"Circle: r = {radius}, Area = {area}")


#     # For Sphere - Volume of a sphere given a radius 

#     radius = input("\nEnter the radius: ")

#     radius = float(radius)

#     do_math_volume = (4 * PI * (radius ** 3))
#     volume =  do_math_volume / 3

#     print(f"Sphere: r = {radius}, Volume = {volume}")


#     # For Rectangle - Area of a rectangle given a height and width

#     height = input("\nEnter the height: ")
#     width = input("Enter the width: ")

#     height = int(height)
#     width = int(width)

#     area = height * width 
#     height = float(height)
#     width = float(width)
#     area = float(area)

#     print(f"Rectangle: Height = {height}, Width = {width}, Area = {area}")


#     # For Square - Area of a square given a side length 

#     lenght = input("\nEnter the side lenght: ")

#     lenght = int(lenght)

#     area = lenght ** 2

#     area = float(area)
#     lenght = float(lenght)

#     print(f"Square: Side Length = {lenght},  Area = {area}")


#     # For Isosceles - Area of an isosceles triangle given the length of one leg 
#     # and the height.

#     leg = input("\nEnter the leg length: ")
#     height = input("Enter the height: ")

#     leg = int(leg)
#     height = int(height)

#     do_math_base = ((leg ** 2 - height ** 2) ** (1 / 2))
#     base = 2 * do_math_base 

#     area = 0.5 * height * base

#     area = float(area)
#     leg = float(leg)
#     height = float(height)

#     print(f"Isosceles Triangle: Leg Length = {leg}, Height = {height}, Area = {area}")


#     # For Equilateral - Area of an equilateral triangle given a side length.

#     length_equ = input("\nEnter the side length: ")

#     length_equ = int(length_equ)

#     do_math_area_of_eq = ((3 ** (1/2) / 4))
#     area_of_eq = do_math_area_of_eq * (length_equ ** 2)

#     area_of_eq = float(area_of_eq)
#     length_equ = float(length_equ)

#     print(f"Equilateral Triangle: Side Length = {length_equ}, Area = {area_of_eq}")


#     # For Trapezoid - Area of a trapezoid given base 1, base 2, and height

#     base_1 = input("\nEnter base 1: ")
#     base_2 = input("Enter base 2: ")
#     height = input("Enter height: ")

#     base_1 = int(base_1)
#     base_2 = int(base_2)
#     height = int(height)

#     do_math_area_of_trapezoid = 1/2 * (base_1 + base_2)
#     area = do_math_area_of_trapezoid * height

#     area = float(area)
#     base_1 = float(base_1)
#     base_2 = float(base_2)
#     height = float(height)

#     print(f"Trapezoid: Base 1 = {base_1}, Base 2 = {base_2}, Height = {height}, Area = {area}\n")

# main()