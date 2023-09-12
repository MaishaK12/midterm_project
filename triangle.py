from geometric_shape import GeometricShape
import math


# Class Triangle extends class GeometricShape
class Triangle(GeometricShape):
    # Constructor for the 3 sides of the triangle
    # Sides are in float
    def __init__(self, side1=3.0, side2=4.0, side3=5.0):
        super().__init__()
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        #
        self.colour = "green"
        self.filled = True

    # Accessor and Mutator for all 3 sides
    def get_side1(self):
        return self.side1

    def set_side1(self, side1):
        self.side1 = side1

    def get_side2(self):
        return self.side2

    def set_side2(self, side2):
        self.side2 = side2

    def get_side3(self):
        return self.side3

    def set_side3(self, side3):
        self.side3 = side3

    # Accessor and Mutator for colour
    def get_colour(self):
        return self.colour

    def set_colour(self, colour):
        self.colour = colour

    # Accessor and Mutator for filled
    def is_filled(self):
        return self.filled

    def set_filled(self, filled):
        self.filled = filled

    # Returns the perimeter of triangle
    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

    # Returns the area of triangle
    def get_area(self):
        s = self.get_perimeter() / 2.0
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    # Method returns string description of triangle
    def __str__(self):
        return "Triangle: side1 = " + str(self.side1) + ", side2 = " + str(self.side2) + ", and side3 = " + str(
            self.side3)


# Create Triangle with default side lengths
t = Triangle()
# Displays Triangle's default side lengths
print(str(t))

# Create Triangle with side lengths 2.0, 3.0, 4.0
t2 = Triangle(2.0, 3.0, 4.0)
# Displays Triangle with side lengths 2.0, 3.0, 4.0
print(str(t2))

# Displays perimeter of Triangle created above
print(t2.get_perimeter())
# Displays area of Triangle created above
print(t2.get_area())

# Prompt user for input
side1 = float(input("Enter side 1: "))
side2 = float(input("Enter side 2: "))
side3 = float(input("Enter side 3: "))
colour = input("Enter colour: ")
filled = input("Is Triangle filled? (Press 1 for yes, and 0 for no): ")
# Convert filled to boolean
filled = True if filled == "1" else False

# Create another Triangle and set properties
t = Triangle(side1, side2, side3)
t.set_colour(colour)
t.set_filled(filled)

# Displays results
print("Area: ", t.get_area())
print("Perimeter: ", t.get_perimeter())
print("Colour: ", t.get_colour())
print("Filled: ", t.is_filled())
