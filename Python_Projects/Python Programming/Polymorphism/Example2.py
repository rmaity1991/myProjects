"""
Decorators, Static and Class Methods
Functions(or methods) are created by def statement.

Though methods works in exactly the same way as a function except one point where method first argument is instance object.

We can classify methods based on how they behave, like

Simple method − defined outside of a class. This function can access class attributes by feeding instance argument:

def outside_func(():
Instance method −

def func(self,)
Class method − if we need to use class attributes

@classmethod
def cfunc(cls,)
Static method − do not have any info about the class

@staticmethod
def sfoo()
Till now we have seen the instance method, now is the time to get some insight into the other two methods,


Class Method
The @classmethod decorator, is a builtin function decorator that gets passed the class it was called on or the 
class of the instance it was called on as first argument. The result of that evaluation shadows your function definition.

Static Method
A static method takes neither a self nor a cls(class) parameter but it’s free to accept an arbitrary number of other parameters.


"""

class SumList(object):
   def __init__(self, my_list):
      self.mylist = my_list
   def __add__(self, other):
     new_list = [ x + y for x, y in zip(self.mylist, other.mylist)]

     return SumList(new_list)
   
   def __repr__(self):
      return str(self.mylist)

aa = SumList([3,6, 9, 12, 15])

bb = SumList([100, 200, 300, 400, 500])
cc = aa + bb # aa.__add__(bb)
print(cc) # should gives us a list ([103, 206, 309, 412, 515])


"""
Inheriting From built-in types
Classes can also inherit from built-in types this means inherits from any built-in and take advantage of all the functionality found there.

In below example we are inheriting from dictionary but then we are implementing one of its method __setitem__. This (setitem) is invoked 
when we set key and value in the dictionary. As this is a magic method, this will be called implicitly.
"""

class MyDict(dict):

   def __setitem__(self, key, val):
      print('setting a key and value!')
      dict.__setitem__(self, key, val)

dd = MyDict()
dd['a'] = 10
dd['b'] = 20

for key in dd.keys():
   print('{0} = {1}'.format(key, dd[key]))





# Mylist inherits from 'list' object but indexes from 1 instead for 0!
class Mylist(list): # inherits from list
   def __getitem__(self, index):
      if index == 0:
         raise IndexError
      if index > 0:
         index = index - 1
         return list.__getitem__(self, index) # this method is called when

# we access a value with subscript like x[1]
   def __setitem__(self, index, value):
      if index == 0:
         raise IndexError
      if index > 0:
      index = index - 1
      list.__setitem__(self, index, value)

x = Mylist(['a', 'b', 'c']) # __init__() inherited from builtin list

print(x) # __repr__() inherited from builtin list

x.append('HELLO'); # append() inherited from builtin list

print(x[1]) # 'a' (Mylist.__getitem__ cutomizes list superclass
               # method. index is 1, but reflects 0!

print (x[4]) # 'HELLO' (index is 4 but reflects 3!