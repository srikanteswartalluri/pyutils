__author__ = 'talluri'

def foo():
    return 4
try:
    int('a')
except ValueError as e:
    print e.message
    print 'Input was not numerical'

#int('a')

try:
    int('a')
except Exception as e:
    print e.message
    print 'Input was not numerical'

try:
    foo('test')
except Exception as e:
    print e.message