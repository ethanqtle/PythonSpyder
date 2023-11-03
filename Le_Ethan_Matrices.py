# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 20:12:56 2023

@author: Ethan
"""

class Rational(object):
    def __init__(self, numer, denom):
        g = self.gcd(numer, denom)
        self.numer = numer // g
        self.denom = denom // g
    
    def gcd(self, num1, num2):
        while num2:
            num1, num2 = num2, num1 % num2
        return num1

    def __add__(self, other):
        nx, dx = self.numer, self.denom
        ny, dy = other.numer, other.denom
        return Rational(nx * dy + ny * dx, dx * dy)

    def __mul__(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __str__(self):
        return '{0}/{1}'.format(self.numer, self.denom)
    
    def __repr__(self):
        return 'Rational({0}, {1})'.format(self.numer, self.denom)


class GenericMatrix(object):
    """Abstract class that operates on matrices with the same types of numbers"""
    
    def __init__(self, matrix):
         self.matrix = matrix
         pass

    def get_row(self):
        return len(self.matrix)

    def get_column(self):
        return len(self.matrix[0])

    def __add__(self, a, b):
        """Adds two elements drawn from matrices"""
        # This abstract method returns nothing as it will be overriden in a concrete subclass
        pass

    def __mul__(self, a, b):
        """For multiplying two elements drawn from matrices"""
        # This abstract method returns nothing as it will be overriden in a concrete subclass
        pass

    def __zero__(self):
        """Abstract method for defining the zero element for the type of matrix."""
        # The abstract method returns nothing as it will be overriden in the concrete subclass
        pass

    def get_zero_matrix(self, row, col):
        return GenericMatrix([[self.__zero__() for _ in range(col)]\
                              for _ in range(row)])
        
    def __addMatrix__(self, other):
        """Adds two matrices with the same types of elements and returns the resulting matrix."""
        result = self.get_zero_matrix(self.get_row(), self.get_column())
        for row in range(result.get_row()):
            for column in range(result.get_column()):
                result.matrix[row][column] = \
                    self.__add__(self.matrix[row][column], other.matrix[row][column])
        return result

    def __multiplyMatrix__(self, other):
        """Multiplies two matrices with the same types of elements and returns the resulting matrix."""
        assert self.get_column() == other.get_row(), \
            "number of rows does not match the number of columns in the second matrix"
        assert type(self) == type(other), "Can only multiply compatible matrices"
        result = self.get_zero_matrix(self.get_row(), other.get_column())
        for i in range(self.get_row()):
            for j in range(other.get_column()):
                for k in range(self.get_column()):
                    product = self.__mul__(self.matrix[i][k], other.matrix[k][j])
                    result.matrix[i][j] = self.__add__(result.matrix[i][j], product)
        return result

    def __str__(self):
        """Returns the string representation of the result"""
        str_matrix = []
        for i in range(self.get_row()):
            str_row = []
            for j in range(self.get_column()):
                str_row.append(str(self.matrix[i][j]))                
            str_matrix.append(str_row)                
        return str(str_matrix)


class IntegerMatrix(GenericMatrix):
    def __init__(self, matrix):
        super().__init__(matrix)
    
    def __add__(self, a, b):
        """Adds two integers and return the sum"""
        return a + b
    
    def __mul__(self, a, b):
        """Multplies two integers and returns the product"""
        return a * b
    
    def __zero__(self):
        """Returns 0 for as an integer"""
        return 0

class RationalMatrix(GenericMatrix):
    def __init__(self, matrix):
        super().__init__(matrix)
        
    def __add__(self, a, b):
        assert isinstance(a, Rational)
        assert isinstance(b, Rational)
        return a + b
    
    def __mul__(self, a, b):
        assert isinstance(a, Rational)
        assert isinstance(b, Rational)
        return a * b
    
    def __zero__(self):
        return Rational(0, 1)
## main
a = IntegerMatrix([[3, 4, 5], [4, 6, 5]])
print("a =", a)
b = IntegerMatrix([[2, 1, 6], [3, 2, 7]])
print("a + b =", a.__addMatrix__(b))
m1 = IntegerMatrix([[1, 2, 3], [4, 5, 6], [1, 1, 1]])
m2 = IntegerMatrix([[1, 1, 1], [2, 2, 2], [0, 0, 0]])
print("m1 =", m1)
print("m2 =", m2)
print("m1 + m2 =", m1.__addMatrix__(m2))
print("m1 * m2 =", m1.__multiplyMatrix__(m2))

mr1 = RationalMatrix([[Rational(1, 5), Rational(1, 6), Rational(1, 7)],
                      [Rational(2, 5), Rational(1, 3), Rational(2, 7)],
                      [Rational(3, 5), Rational(1, 2), Rational(3, 7)]])

mr2 = RationalMatrix([[Rational(1, 6), Rational(1, 7), Rational(1, 8)],
                      [Rational(1, 3), Rational(2, 7), Rational(1, 4)],
                      [Rational(1, 2), Rational(3, 7), Rational(3, 8)]])

print("mr1 =", mr1)
print("mr2 =", mr2)
print("mr1 + mr2 =", mr1.__addMatrix__(mr2))
print("mr1 * mr2 =", mr1.__multiplyMatrix__(mr2))