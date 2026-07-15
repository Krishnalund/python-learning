# Create a class with a class attribute a; create an object from it and set ‘aʼ directly using
# ‘object.a = 0ʼ. Does this change the class attribute?

# Answer: The class attribute does not change

class Example:
    a = 4          # class attribute

object1 = Example()
object1.a = 0      # instance attribute

object2 = Example()

print(Example.a)
print(object1.a)
print(object2.a)
