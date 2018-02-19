# Q5. Define an Student class and initialize it with name and section.
# Now, make a classmethod that takes in a string parameter "name-A" which creates an instance and returns the instance based on parameter.
#  [Hint: use @classmethod decorator]

class Student:
    def __init__(self,name,section):
        self.name = name
        self.section= section

    @classmethod
    def getObjFromString(cls,inp):
        name,section= inp.split("-")
        return cls(name,section)

    def getname(self):
        return self.name
    def getSection(self):
        return self.section

emp= Student.getObjFromString("Supriya-B")
print(emp.getname())
print(emp.getSection())

