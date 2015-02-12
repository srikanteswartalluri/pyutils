__author__ = 'talluri'

class Animal:
    def __init__(self,eyes,legs):
        self.eyes = eyes
        self.legs = legs
        self.flies = False
    def fly(self):
        return self.flies

class Monkey(Animal):
    def __init__(self,eyes,legs,hands):
        Animal.__init__(self,eyes,legs)
        self.hands = hands
    def __repr__(self):
        return 'Monkey <eyes: {}, legs: {}, hands: {}>'.format(self.eyes, self.legs, self.hands)
class Squirrel(Animal):
    def __init__(self,eyes,legs):
        Animal.__init__(self,eyes,legs)
    def __repr__(self):
        return 'Squirrel <eyes: {}, legs: {}>'.format(self.eyes, self.legs)

class Pigeon(Animal):
    def __init__(self,eyes,legs,fly,wings):
        Animal.__init__(self,eyes,legs)
        self.flies = fly
        self.wings = wings
    def __repr__(self):
        return 'Pigeon <fly: {}, eyes: {}, legs: {}, wings: {}>'.format(self.flies, self.eyes, self.legs, self.wings)


class Eagle(Animal):
    def __init__(self,eyes,legs,fly,wings):
        Animal.__init__(self,eyes,legs)
        self.flies = fly
        self.wings = wings
    def __repr__(self):
        return 'Eagle <fly: {}, eyes: {}, legs: {}>'.format(self.flies, self.eyes, self.legs, self.wings)




class Ladder:

    def __init__(self):
        self.rungs = [None]*20
    def __repr__(self):
        pass
    def populate(self, animal, rung):
        self.rungs[rung] = animal

    def animal_at_rung(self,rung):
        return self.rungs[rung]

    def get_animals_count(self):
        i = 0
        for rung in range(len(self.rungs)):
            if self.rungs[rung] is not None:
                i = i + 1
        return i
    def hop(self,rung):
        '''
        move the animal to the next rung if empty
        '''
        if self.rungs[rung] is None:
            self.rungs[rung] = self.rungs[rung-1]
            self.rungs[rung-1] = None
        else:
            print "Not Empty"


ladder = Ladder()
ladder.populate(Monkey(2,2,2) ,3)
ladder.populate(Squirrel(2,2),5)
ladder.populate(Pigeon(2,2,'True',2),8)
ladder.populate(Eagle(2,2,'True',2),15)
ladder.populate(Monkey(2,2,2),17)
