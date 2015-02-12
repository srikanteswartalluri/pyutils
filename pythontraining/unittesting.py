__author__ = 'talluri'
def sum(*args):
    if len(args) == 0:
        return None
    s = 0
    for arg in args:
        s += arg
    return s


