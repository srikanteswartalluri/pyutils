class Person:
    def __init__(self):
        self.A = 'Sri'
        self.__B = 'Talluri'
    def PrintName(self):
        print 'public=>%s' %self.A
        print 'Private=>%s' %self.__B

    def __Hidden(self):
        print 'I am in hidden=>'
        self.PrintName()
    def test(self):
        print 'I am in test'
        self.__Hidden()

p = Person()
p.PrintName()
print 'Access public outside=>%s' %p.A
# print 'Access private outside=>%s' %p.__B #expected failure
print 'hidden=>',p._Person__B
p.test()
#p.__Hidden() #expected failure
p._Person__Hidden()#a way to access hidden function