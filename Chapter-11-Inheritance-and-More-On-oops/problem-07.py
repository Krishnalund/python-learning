# Override the __len__() method on vector of problem 5 to display the dimension of the vector.

class Vector:
    def __init__(self,vector):
        self.vector = vector

    def __add__(self, other):
        result = []
        for x,y in zip(self.vector, other.vector):
            result.append(x + y)
        return Vector(result)
    
    def __mul__(self, other):
        total = 0
        for x,y in zip(self.vector, other.vector):
            total += x * y
        return total

    def __str__(self):
        return str(self.vector)
    
    def __len__(self):
        return len(self.vector)
    
v1 = Vector([2,3,4])
v2 = Vector([4,5,6])
v3 = v1 + v2
v4 = v1 * v2
print(v3)
print(v4)
print('Length of Vector:',len(v1))