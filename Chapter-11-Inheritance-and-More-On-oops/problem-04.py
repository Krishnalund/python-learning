# Write a class ‘Complexʼ to represent complex numbers, along with overloaded operators
# ‘+ʼ and ‘*ʼ which adds and multiplies them.

class Complex:
    def __init__(self, real , imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(
            self.real + other.real,
            self.imaginary + other.imaginary
        )
    
    def __mul__(self, other):
        return Complex(
            (self.real * other.real) - (self.imaginary * other.imaginary),
            (self.real * other.imaginary) + (self.imaginary * other.real)
        )
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"
    
c1 = Complex(2,3)
c2 = Complex(4,5)
c3 = c1 + c2
c4 = c1 * c2
print(c3)
print(c4)
