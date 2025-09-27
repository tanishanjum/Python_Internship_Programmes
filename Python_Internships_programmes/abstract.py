#Abstraction
# it is the concept of hiding the implementation part and show only functionality to the user
#abstract class contain abstract method
from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat():
        pass
    @abstractmethod
    def sound():
        pass

class Lion(Animal):
    def eat():
        print("Lion eat flesh")
    def sound():
        print("Lion roars")

class Dog(Animal):
    def eat():
        print("Dog eat pedegree")
    def sound():
        print("Dog barks")

obj=Lion
obj.eat()
obj.sound()
