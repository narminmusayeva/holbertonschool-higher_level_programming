Python - Inheritance
What is Inheritance?
Inheritance is one of the core concepts of Object-Oriented Programming (OOP). It allows one class (called the child or subclass) to inherit attributes and methods from another class (called the parent or superclass). This promotes code reuse and helps in creating a hierarchical structure for classes.

Benefits of Inheritance:
Avoid code repetition: Common functionality can be placed in a parent class and reused by child classes.
Better organization: Helps structure the code in a way that is easy to maintain and extend.
Code reuse: For example, an Animal class can be inherited by Dog, Cat, or Bird classes, where common behaviors are inherited, and specific ones can be added.
Implementing Inheritance in Python
In Python, inheritance is implemented by defining a subclass that takes the parent class as an argument. Here's an example:

class ParentClass:
def **init**(self, name):
self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}")

# Child class inherits from ParentClass

class ChildClass(ParentClass):
def **init**(self, name, age):
super().**init**(name) # Calls the constructor of the parent class
self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

Explanation:
ParentClass: This is the parent class that defines the method greet and the name attribute.
ChildClass: This is the child class that inherits from ParentClass. It inherits the name attribute and greet method, while adding a new attribute age and a new method introduce.
super(): The super() function is used to call the parent class’s methods from the child class. In this case, it calls the **init** method of the ParentClass to initialize the name attribute.
Key Features of Inheritance:
Child Classes: Classes that inherit from other classes are known as child classes.
Parent Classes: The class that is being inherited from is called the parent class.
super() function: Used to call methods and attributes from the parent class in the child class.
Override: Child classes can override (redefine) methods from the parent class.
Example of Overriding Methods:
python
Kopyala
Düzenle
class Animal:
def **init**(self, name):
self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
def speak(self):
print(f"{self.name} barks")

class Cat(Animal):
def speak(self):
print(f"{self.name} meows")

# Using inheritance

dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak() # Output: Buddy barks
cat.speak() # Output: Whiskers meows
In this example:

The Animal class defines a general speak method.
The Dog and Cat classes inherit from the Animal class but override the speak method to provide their own specific behavior.
Conclusion:
Inheritance is a fundamental feature of object-oriented programming that allows for the reuse of code and the creation of more organized and extensible programs. Python makes inheritance easy to implement with the class syntax and the super() function.

