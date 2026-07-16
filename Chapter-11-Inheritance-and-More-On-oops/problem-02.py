# Create a class ‘Petsʼ from a class ‘Animalsʼ and further create a class ‘Dogʼ from ‘Petsʼ.
# Add a method ‘barkʼ to class ‘Dogʼ.

class Animals:
    def sound(self):
        print('Some sound')

class Pets(Animals):
    pass

class Dog(Pets):
    def bark(self):
        print('Bark')

d = Dog()
d.sound()
d.bark()