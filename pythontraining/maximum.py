__author__ = 'talluri'
def maximum(*args):
    maxval = args[0]
    for i in args[1:]:
        if i > maxval:
            maxval = i
    return maxval
def mv(*args):
    mval = args[0]
    i = 0
    while i < len(args):
        if mval < args[i]:
            mval = args[i]
        i = i+1
    return mval
p = maximum(1,3,4,5,7)

print p
q = mv(3,4,6,8)
print q

