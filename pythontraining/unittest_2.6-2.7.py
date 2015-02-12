__author__ = 'talluri'
import sys

if sys.version_info >= (2, 7):
    import unittest
else:
    try:
        import unittest2 as unittest
    except:
        print 'python version is < 2.7 and unittest2 is not detected'
        sys.exit(1)
