from pkg_resources import WorkingSet , DistributionNotFound
working_set = WorkingSet()

# Printing all installed modules
print tuple(working_set)

# Detecting if module is installed
try:
    dep = working_set.require('paramiko>=1.0')
except DistributionNotFound:
    pass

# Installing it (anyone knows a better way?)
from setuptools.command.easy_install import main as install
install(['django>=1.2'])
