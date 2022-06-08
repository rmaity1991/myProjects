"""
Like other general-purpose programming languages, Python is also an object-oriented language since its beginning. 
It allows us to develop applications using an Object-Oriented approach. In Python, we can easily create and use classes and objects.

An object-oriented paradigm is to design the program using classes and objects. 
The object is related to real-word entities such as book, house, pencil, etc. The oops concept focuses on writing the reusable code. 
It is a widespread technique to solve the problem by creating objects.

Major principles of object-oriented programming system are given below.

Class
Object
Method
Inheritance
Polymorphism
Data Abstraction
Encapsulation

"""

class car:  
    def __init__(self,modelname, year):  
        self.modelname = modelname  
        self.year = year  
    def display(self):  
        print(self.modelname,self.year)  
  
c1 = car("Toyota", 2016)  
c1.display()  

"""
Inheritance
Inheritance is the most important aspect of object-oriented programming, which simulates the real-world concept of inheritance. 
It specifies that the child object acquires all the properties and behaviors of the parent object.

By using inheritance, we can create a class which uses all the properties and behavior of another class. The new class is known 
as a derived class or child class, and the one whose properties are acquired is known as a base class or parent class.

It provides the re-usability of the code.

Polymorphism
Polymorphism contains two words "poly" and "morphs". Poly means many, and morph means shape. By polymorphism, we understand that 
one task can be performed in different ways. For example - you have a class animal, and all animals speak. But they speak differently. 
Here, the "speak" behavior is polymorphic in a sense and depends on the animal. So, the abstract "animal" concept does not actually "speak", 
but specific animals (like dogs and cats) have a concrete implementation of the action "speak".

Encapsulation
Encapsulation is also an essential aspect of object-oriented programming. It is used to restrict access to methods and variables. 
In encapsulation, code and data are wrapped together within a single unit from being modified by accident.

Data Abstraction
Data abstraction and encapsulation both are often used as synonyms. Both are nearly synonyms because data abstraction is achieved 
through encapsulation.

Abstraction is used to hide internal details and show only functionalities. Abstracting something means to give names to things 
so that the name captures the core of what a function or a whole program does.
"""