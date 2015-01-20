__author__ = 'talluri'
l = []
for i in range(-5, 5):
    l.append(i)
print l

m = filter((lambda x: x < 0), l)

print m


