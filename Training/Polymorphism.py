class Animal:
    def name(self):
        pass
    def sleep(self):
        print 'sleep'
    def MakeNoise(self):
        pass
class Dog(Animal):
    def name(self):
        print 'I am a dog'
    def MakeNoise(self):
        print 'woof'
class Cat(Animal):
    def name(self):
        print 'I am a cat'
    def MakeNoise(self):
        print 'meow'
class Lion(Animal):
    def name(self):
        print 'I am a lion'
    def MakeNoise(self):
        print 'roar'

class TestAnimals:
    def PrintName(self, animal):
        animal.name()
    def TestNoise(self, animal):
        animal.MakeNoise()
    def TestSleep(self, animal):
        animal.sleep()

cat = Cat()
dog = Dog()
lion = Lion()
repr(lion)

tc = TestAnimals()

tc.PrintName(cat)
tc.TestSleep(cat)
tc.TestNoise(cat)


tc.PrintName(dog)
tc.TestSleep(dog)
tc.TestNoise(dog)


tc.PrintName(lion)
tc.TestSleep(lion)
tc.TestNoise(lion)


