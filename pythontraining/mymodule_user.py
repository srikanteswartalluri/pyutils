__author__ = 'talluri'
import mymodule

print mymodule.VERSION

print mymodule.version()

from mymodule import *#not a good practice, it pollutes local name space

print VERSION

print version()
