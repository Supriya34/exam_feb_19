
#
# Q2. Create a class Circle which has a class variable PI with the value=22/7.
# Make two methods getArea and getCircumference inside this Circle class.
# Which when invoked returns area and circumference of each circle instances.

class Circle:
    PI= 22/7
    def __init__(self,radius):
        self.radius=radius

    def getArea(self):
        return self.PI* self.radius**2

    def getCircumference(self):
        return 2* self.PI * self.radius


cir= Circle(2)
print("The area is : {}".format(cir.getArea()))
print("The circumference is : {}".format(cir.getCircumference()))
