__author__ = 'talluri'

class Person():
    counter = 0
    def __init__(self):
        Person.counter +=1

    @classmethod
    def printCounter(cls):
        print cls.counter
    @staticmethod
    def printlesscount():
        print Person.counter

p = Person()

Person.printCounter()
p.printCounter()

p1 = Person()

Person.printCounter()
p1.printCounter()
p2 = Person()
p2.printCounter()

Person.printlesscount()
Person.printlesscount()