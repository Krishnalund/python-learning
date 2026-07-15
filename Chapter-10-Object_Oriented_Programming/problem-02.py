# Write a class “Calculator” capable of finding square, cube and square root of a number.
class Calculator:
    def __init__(self , num):
        self.num = num

    def square(self):
        return self.num ** 2
    
    def cube(self):
        return self.num ** 3

    def square_root(self):
         return (self.num)** 0.5

calc_obj = Calculator(4)
print(calc_obj.square())
print(calc_obj.cube())
print(calc_obj.square_root())

