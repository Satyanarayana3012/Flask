class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

animal = Animal()
animal.speak()

dog = Dog()
dog.speak()