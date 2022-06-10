import sys

print('Previous code with exception handling')

try:
   number = int(input('Enter number between 1 > 10: '))

except(ValueError):
   print('Error..numbers only')
   sys.exit()

print('You have entered number: ',number)



def enterAge(age):
   if age<0:
      raise ValueError('Only positive integers are allowed')
   if age % 2 ==0:
      print('Entered Age is even')
   else:
      print('Entered Age is odd')

try:
   num = int(input('Enter your age: '))
   enterAge(num)
except ValueError:
   print('Only positive integers are allowed')


class NegativeNumberException(RuntimeError):
   def __init__(self, age):
      super().__init__()
      self.age = age


def enterage(age):
   if age < 0:
      raise NegativeNumberException('Only positive integers are allowed')

   if age % 2 == 0:
      print('Age is Even')

   else:
      print('Age is Odd')

try:
   num = int(input('Enter your age: '))
   enterage(num)
except NegativeNumberException:
   print('Only positive integers are allowed')
except:
   print('Something is wrong')