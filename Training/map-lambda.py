__author__ = 'talluri'
def squ(x):
    return x*x
def cub(x):
    return x*x*x
p = map(squ, [1, 2, 3])

print p

#with lambda

q = map((lambda x: x*x), [1, 2, 3])

print q

#map with two arguments to a function
t = map(pow, [1, 2, 3], [1, 2, 3])

print t

#functions as a list
fun = [squ, cub]
for i in range(5):
    s = map((lambda x: x(i)), fun)
    print s
