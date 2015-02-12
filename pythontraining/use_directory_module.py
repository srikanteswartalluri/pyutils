__author__ = 'talluri'
import day2dir.mymodule

print day2dir.mymodule.VERSION

from day2dir.mymodule import version

print version()

import day2dir.subdirmod.mymodule

print dir(day2dir.subdirmod)
print dir(day2dir)

print day2dir.__name__,day2dir.__file__



