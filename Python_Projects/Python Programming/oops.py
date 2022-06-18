import math as mt

class Circle:


    def __init__(self,radius=1):
        self.radius=radius

    def area(self)->float:
        print("The area of the circle is {}".format(pow(self.radius,2)*mt.pi))
        return (pow(self.radius,2)*mt.pi)




test=Circle()

result=test.area()

print(result)