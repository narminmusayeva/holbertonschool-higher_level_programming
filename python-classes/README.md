# Python Classes

In Python, a **class** is a fundamental part of object-oriented programming (OOP). Classes are used to create objects that share common attributes and methods.

## Classes and Objects

- **Class**: A blueprint or template for creating objects.
- **Object**: An instance of a class.

### Creating a Class

```python
class MyClass:
    x = 5

obj = MyClass()
print(obj.x)  # 5
```

### The `__init__` Method

The `__init__` method is a special method that runs automatically when an object is created.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Alice", 25)
print(p1.name)  # Alice
```

### Methods and `self`

Methods can be defined within a class. The `self` parameter represents the instance of the class.

```python
class Car:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print(f"Car brand: {self.brand}")

car1 = Car("Toyota")
car1.show_brand()  # Car brand: Toyota
```

### Inheritance

A class can inherit attributes and methods from another class.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Bark!")

my_dog = Dog()
my_dog.speak()  # Bark!
```

### Conclusion

Python classes help organize code, making it more structured and reusable. Learning OOP principles makes coding more efficient and flexible.
