__author__ = 'talluri'
def foo():
    print 'Hello'

bar = foo

bar()
#functions are first class which means we can use functions as any other variable


#function with in a function
def foodGen():
    def food():
        print 'Hello inside foodgen:foo'
    return food

print foodGen()
fgen = foodGen()

fgen()
print fgen
foodGen()()


fgen = 10
print fgen

#passing function to a function
def foo_caller(foo):
    foo()

def myfunc():
    print 'inside my func'
foo_caller(myfunc)

