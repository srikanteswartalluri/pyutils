__author__ = 'talluri'

class Person:
    def __init__(self, name):
        self.name = name
    def printDetails(self):
        print self.name

class Employee(Person):
    def __init__(self, name, employeeID):
        Person.__init__(self,name)
        self.employeeId = employeeID

e = Employee('talluri', '14978')

print e.name, e.employeeId