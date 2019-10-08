class Virus(object):
    '''Properties and attributes of the virus used in Simulation.'''

    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate

#Tests virus attributes
# virus = Virus("TB", 0.6, 0.3)
# print(virus.name)
# print(virus.mortality_rate)
# print(virus.repro_rate)
