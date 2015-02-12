__author__ = 'talluri'
from ladderutils import ladder

print ladder.animal_at_rung(3)
print ladder.animal_at_rung(5)
print ladder.animal_at_rung(8)
print ladder.animal_at_rung(15)
print ladder.animal_at_rung(10)
print ladder.get_animals_count()
print ladder.animal_at_rung(3) == ladder.animal_at_rung(17)
print type(ladder.animal_at_rung(3)) == type(ladder.animal_at_rung(17))
print ladder.animal_at_rung(8).fly()
print ladder.animal_at_rung(3).fly()
print ladder.hop(3)
print ladder.animal_at_rung(3)
print ladder.animal_at_rung(4)
print ladder.hop(4)
print ladder.animal_at_rung(4)
