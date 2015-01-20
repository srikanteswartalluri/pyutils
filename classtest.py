class Test():
    testVar = None
    def __init__(self, test):
        self.testVar = test


t = Test(4)
print t.testVar
print Test.testVar



t.testVar = 6

print t.testVar
print Test.testVar

Test.testVar = 11

print t.testVar
print Test.testVar