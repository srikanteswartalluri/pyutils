class Person:
    # @classmethod
    # def speak(cls):
    #     print cls().__class__, '=>I can speak'

    def speak(self):
        print self.__class__, '=>I can speak'

class Man(Person):
    def wear(self):
        print self.__class__, '=>I wear shirt'

class Woman(Man):
    def wear(self):
        print self.__class__, '=>I wear skirt'

man = Man()
woman = Woman()

man.speak()
man.wear()
woman.wear()
Person().speak()

