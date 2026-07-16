# Write __str__() method to print the vector as follows: 7i + 8j + 10k

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
        return f"{self.vector[0]}i + {self.vector[1]}j + {self.vector[2]}k"
    
v1 = Vector([2,3,4])
v2 = Vector([4,5,6])
v3 = v1 + v2
v4 = v1 * v2
print(v3)
print(v4)
