__author__ = 'talluri'
a = 2
b = 3
def swap(a, b):
    a, b = b, a
    print "a:",a
    print "b:",b

swap(a,b)

print "a:",a
print "b:",b

# call by reference of the value

l = [1,2,3]
def appendTo(l,num):
    l.append(num)
appendTo(l,4)
print l

