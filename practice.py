# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")

# animal = Animal()
# animal.speak()

# dog = Dog()
# dog.speak()

class Shape:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return 0

class Rectangle(Shape):
    def area(self):
        return self.width * self.height

rectangle = Rectangle(5, 8)

print(rectangle.area()) 