import random
random.seed(42) 
#random seed sets a random number so that it always stays the same, comment 
#this out to test float values. Thx stack overflow for the clearification
from virus import Virus


class Person(object):
    ''' Person objects will populate the simulation. '''

    def __init__(self, _id=None, is_vaccinated=None, infection=None):
        ''' We start out with is_alive = True, because we don't make vampires or zombies.
        All other values will be set by the simulation when it makes each Person object.

        If person is chosen to be infected when the population is created, the simulation
        should instantiate a Virus object and set it as the value
        self.infection. Otherwise, self.infection should be set to None.
        '''
        self._id = _id  # int
        self.is_alive = True  # boolean
        self.is_vaccinated = is_vaccinated  # boolean
        self.infection = infection  # Virus object or None

    def did_survive_infection(self):
        chance = random.uniform(0, 1)
        if chance < self.infection.mortality_rate:
            return False
        # Only called if infection attribute is not None.
        if self.infection == None:
            self.is_vaccinated = True
        # TODO: Do we need to return None is off case senerios? 
        return True



#tests random floats in terminal
# test_chance = random.uniform(0, 1)
# print(test_chance)
#Thanks pynative for teaching me random.uniform

#tests moved into test.py to reorganize code