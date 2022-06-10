"""

Polymorphism is an important feature of class definition in Python that is utilized when you have commonly named methods across 
classes or subclasses. This permits functions to use entities of different types at different times. So, it provides flexibility and 
loose coupling so that code can be extended and easily maintained over time.

This allows functions to use objects of any of these polymorphic classes without needing to be aware of distinctions across the classes.

Polymorphism can be carried out through inheritance, with subclasses making use of base class methods or overriding them.

Let understand the concept of polymorphism with our previous inheritance example and add one common method called show_affection in 
both subclasses −

From the example we can see, it refers to a design in which object of dissimilar type can be treated in the same manner or more 
specifically two or more classes with method of the same name or common interface because same method(show_affection in below example) is 
called with either type of objects.

Overriding
In Python, when a subclass contains a method that overrides a method of the superclass, you can also call the superclass method by calling

Super(Subclass, self).method instead of self.method.


"""

class Thought(object):
   def __init__(self):
      pass
   def message(self):
      print("Thought, always come and go")

class Advice(Thought):
   def __init__(self):
      super(Advice, self).__init__()
   def message(self):
      print('Warning: Risk is always involved when you are dealing with market!')

"""
Inheriting the Constructor
If we see from our previous inheritance example, __init__ was located in the parent class in the up ‘cause the child class dog or cat 
didn’t‘ve __init__ method in it. Python used the inheritance attribute lookup to find __init__ in animal class. When we created the child 
class, first it will look the __init__ method in the dog class, then it didn’t find it then looked into parent class Animal and found there 
and called that there. So as our class design became complex we may wish to initialize a instance firstly processing it through parent 
class constructor and then through child class constructor.
__init__ is like any other method; it can be inherited

If a class does not have a __init__ constructor, Python will check its parent class to see if it can find one.

As soon as it finds one, Python calls it and stops looking

We can use the super () function to call methods in the parent class.

We may want to initialize in the parent as well as our own class.
"""
