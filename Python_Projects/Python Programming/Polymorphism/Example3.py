"""
Variable Naming − ‘Public’ and ‘Private’
In Python, when we are dealing with modules and classes, we designate some variables or attribute as private. In Python, 
there is no existence of “Private” instance variable which cannot be accessed except inside an object. Private simply means 
they are simply not intended to be used by the users of the code instead they are intended to be used internally. In general, 
a convention is being followed by most Python developers i.e. a name prefixed with an underscore for example. _attrval (example below) 
should be treated as a non-public part of the API or any Python code, whether it is a function, a method or a data member. Below is 
the naming convention we follow,

Public attributes or variables (intended to be used by the importer of this module or user of this class) −regular_lower_case

Private attributes or variables (internal use by the module or class) −_single_leading_underscore

Private attributes that shouldn’t be subclassed −__double_leading_underscore

Magic attributes −__double_underscores__(use them, don’t create them)

"""

class GetSet(object):

   instance_count = 0 # public
   
   __mangled_name = 'no privacy!' # special variable

   def __init__(self, value):
      self._attrval = value # _attrval is for internal use only
      GetSet.instance_count += 1

   @property
   def var(self):
      print('Getting the "var" attribute')
      return self._attrval

   @var.setter
   def var(self, value):
      print('setting the "var" attribute')
      self._attrval = value

   @var.deleter
   def var(self):
      print('deleting the "var" attribute')
      self._attrval = None

cc = GetSet(5)
cc.var = 10 # public name
print(cc._attrval)
print(cc._GetSet__mangled_name)