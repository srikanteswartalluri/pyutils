__author__ = 'talluri'

def foo(a,b,*args, **kwargs1):
    print kwargs1
    print args
    print type(args)
    print type(kwargs1)
    print "#"*50

foo(1,2)
foo(a=3, b=4)
foo(3,5,6,k=55,r=44)
#foo(a=3, b=4,5,6,c=4,f=6)
#foo(t=5,3)
