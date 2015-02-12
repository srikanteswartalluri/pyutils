__author__ = 'talluri'
class MyException(Exception):
    pass

try:
    int('a')
except ValueError as e:
    raise MyException(e)
finally:
    print 'Finally got executed'

print 'will never get executed'