class A:
    def Am(self):
        print self.__class__, '=>I am in A'
class B(A):
    def Am(self):
        print self.__class__, '=>I am in Am'
    def Bm(self):
        print self.__class__, '=>I am in Bm'
class C(A, B):
    def Cm(self):
        print self.__class__, '=>I am in Cm'

a = A()
b = B()
c = C()


c.Am()
c.Bm()
c.Cm()
