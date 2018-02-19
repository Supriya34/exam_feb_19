
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


    def emailGenerator(self):
        self.email = self.fname.lower()+'.'+self.lname.lower()+'@deerwalk.edu.np'

    def displayInfo(self):
        print("First name: {}\nLast name: {}\n The Email generated is : {}".format(self.fname, self.lname, self.email))


emp1 = Employee(input('Enter first name: '), input('Enter last name: '))
emp1.emailGenerator()
emp1.displayInfo()