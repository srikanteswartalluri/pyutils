__author__ = 'talluri'
def foo(x,y,p=10,q=20):
     print x
     print y
     print p
     print q

foo(3,5)
foo(3,5,40)
foo(3,5,40,60)
foo(3,5,q=50)

