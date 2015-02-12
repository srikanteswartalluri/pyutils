class Person:
    def __init__(self, name):
        self.name = name
    def SayHello(self):
        print 'Hello, my name is %s' %self.name
    def SayBi(self):
        print 'Good Bye %s' % self.name
        print 'my classmethod var %s' %self.__class__.test
    @classmethod
    def MyClassMethod(cls):
        cls.test = "myvar"

p = Person('SrikanteswaraRao Talluri')
Person.MyClassMethod()
p.SayHello()
p.SayBi()

print 'class=>', p.__class__
print "dict=>", p.__dict__
print "doc=>", p.__doc__
print 'module=>', p.__module__
print 'name=>', p.__class__.__name__
# print 'bases=>', p.__bases__


class A:
    #i = 23
    def __init__(self):
        self.p = 12345
    @classmethod
    def CM(cls):
        cls.i = 44

    def testCM(self):
        print self.__class__.__name__, ".i=> %s" % self.i

#Invoke form
# print 'invoke form=>', A.i
A.p = 4


a = A()
a.p = 5
A.CM()
a.testCM()
A.testCM()
#Invoke Object
print 'invoke form=>', A.i
print 'invoke object=>', A().i


