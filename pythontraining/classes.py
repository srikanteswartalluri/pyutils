__author__ = 'talluri'

def display():
    print 'display'

class Person:
    def print_name(pell):
        print pell.name

p = Person()
p.name = 'Talluri'
p.print_name()
print p.print_name
p.displayname = display
print p.__dict__

Person.print_name(p)

q = Person()
q.name = 'Srikanti'

Person.print_name(q)