# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 16:07:02 2023

@author: Ethan
"""
from datetime import datetime
import math

class GeometricObjects:
    def __init__(self, color = "blue", filled = True):
        self.color = color
        self.filled = filled
        self.dateCreated = datetime.now()
        
    def get_dateCreated(self):
        return self.dateCreated
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color
        
    def get_filled(self):
        return self.filled
    
    def set_filled(self, filled):
        self.filled = filled
    
    def __str__(self):
        class_name = self.__class__.__name__.lower()
        ret_list = [f"A {class_name} was created on {self.get_dateCreated()}"
                    ,f"Color of {class_name} is {self.get_color()}"
                    ,f"Filled: {self.get_filled()}"]
        return "\n".join(ret_list)

class Circle(GeometricObjects):
    def __init__(self, user_radius, color = "blue", filled = True):
        super().__init__(color, filled)
        self.radius = user_radius
        
    def get_radius(self):
        return self.radius
    
    def set_radius(self, user_radius):
        self.radius = user_radius
        
    def get_area(self):
        return math.pi * self.radius * self.radius
    
    def get_perimeter(self):
        return 2 * math.pi * self.radius
    
    def __str__(self):
        ret_list = [super().__str__(), 
                    f"The radius is {self.get_radius()}", 
                    f"The area is {self.get_area()}", 
                    f"The perimeter is {self.get_perimeter()}"]
        return "\n".join(ret_list)
        
class Rectangle(GeometricObjects):
    def __init__(self, width = 4.0, height = 2.0,  color = "red", filled = False):
        super().__init__(color, filled)
        self.width = width
        self.height = height
        
    def get_width(self):
        return self.width
    
    def set_width(self, width):
        self.width = width
      
    def get_height(self):
        return self.height
    
    def set_height(self, height):
        self.height = height
        
    def get_perimeter(self):
        return self.height * 2 + self.width * 2
    
    def get_area(self):
        return self.height * self.width
        
    def __str__(self):
        ret_list = [super().__str__(), 
                    f"The width is {self.get_width()}",
                    f"The height is {self.get_height()}",
                    f"The area is {self.get_area()}", 
                    f"The perimeter is {self.get_perimeter()}"]
        return "\n".join(ret_list)
    
user_radius = float(input("Please enter the radius of your circle: "))
circle = Circle(user_radius)
print(circle)

rectangle = Rectangle(4.0, 2.0)  # You can specify the width and height here
print(rectangle)