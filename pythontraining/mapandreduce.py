__author__ = 'talluri'

def square(name):
    return name*name

lists = [2,3,4,5,6,]


newlist = map(square,lists)

print newlist

fibSeries = {}
def fib(n):
    if n <= 1:
        return n
    if n not in fibSeries:
        fibSeries[n] = fib(n-1) + fib(n-2)
    return fibSeries[n]

print map(fib,range(10))
