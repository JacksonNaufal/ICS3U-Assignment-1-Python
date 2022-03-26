#!/usr/bin/env python3

# Created by: Jackson Naufal
# Created on: March 2022
# This is a calculator for the perimeter of a triangle


def main():
    # This is a calculator that calculates the area and perimeter of a rectangle
    # input
    print(
        "This is a perimeter of a triangle calculator, please input"
        "your triangles values down below!"
    )
    sideA = int(input("\nEnter side A of rectangle (mm): "))
    sideB = int(input("Enter side B of rectangle (mm): "))
    sideC = int(input("Enter side C of rectangle (mm): "))

    # process
    trianglePerimeter = sideA + sideB + sideC

    # output
    print("\nYour equation, for your triangle is")
    print("\nP = a + b + c")
    print("P = {0} + {1} + {2}".format(sideA, sideB, sideC))
    print("P = {0} mm".format(trianglePerimeter))
    print("\nThe perimeter of your triangle is {0} mm.".format(trianglePerimeter))
    print("\nDone.")


if __name__ == "__main__":
    main()
