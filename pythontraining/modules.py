__author__ = 'talluri'

import math

print dir(math)

print math.sqrt(4)
print type(math.sqrt(4))

print type(math.sqrt)

print math.pi

import random

print dir(random)

print random.random()

import sys

print sys.argv
print len(sys.argv)
print sys.path
print len(sys.path)
sys.path.append('/Users/talluri')
print sys.path
if '/Users/talluri' in sys.path:
    print 'found'
else:
    print 'not found'



print "#"*50

from math import pi

print pi

from random import random

print random

import sys

print sys.stdout
print type(sys.stdout)
from sys import stdout

print stdout

pi = 3.14

from math import pi as mathpi
print pi
print mathpi
from math import pi

print pi

