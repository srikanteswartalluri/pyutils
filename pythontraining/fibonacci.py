__author__ = 'talluri'

fibSeries = {}
def fib(n):
    if n <= 1:
        return n
    if n not in fibSeries:
        fibSeries[n] = fib(n-1) + fib(n-2)
    return fibSeries[n]
        #return fib(n-2) + fib(n-1) if n>1 else n



num = raw_input('enter the num')
num.rstrip()
retVal = fib(int(num))
print retVal
# for f in  fibSeries:
#     print f
