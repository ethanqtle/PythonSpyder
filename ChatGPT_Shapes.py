from datetime import datetime

class GeometricObject:
    def __init__(self, color="blue", filled=True):
        self.__color = color
        self.__filled = filled
        self.__dateCreated = datetime.now()

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def is_filled(self):
        return self.__filled

    def set_filled(self, filled):
        self.__filled = filled

    def get_date_created(self):
        return self.__dateCreated

    def __str__(self):
        return f"Color of {self.__class__.__name__.lower()} is {self.__color}\nFilled: {self.__filled}\nThe date created is {self.__dateCreated}"

class Circle(GeometricObject):
    def __init__(self, radius, color="blue", filled=True):
        super().__init__(color, filled)
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_area(self):
        return round(3.1415926 * self.__radius * self.__radius, 7)

    def get_perimeter(self):
        return round(2 * 3.1415926 * self.__radius, 7)

    def __str__(self):
        return f"A circle was created on {super().get_date_created()}\n{super().__str__()}\nThe radius is {self.__radius}\nThe area is {self.get_area()}\nThe perimeter is {self.get_perimeter()}"

class Rectangle(GeometricObject):
    def __init__(self, width, height, color="red", filled=False):
        super().__init__(color, filled)
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_area(self):
        return self.__width * self.__height

    def get_perimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        return f"A rectangle was created on {super().get_date_created()}\n{super().__str__()}\nThe width is {self.__width}\nThe height is {self.__height}\nThe area is {self.get_area()}\nThe perimeter is {self.get_perimeter()}"

# Main program
radius = float(input("Enter the radius of your circle: "))
circle = Circle(radius)
rectangle = Rectangle(4.0, 2.0)  # You can specify the width and height here

print("\nCircle:")
print(circle)

print("\nRectangle:")
print(rectangle)
