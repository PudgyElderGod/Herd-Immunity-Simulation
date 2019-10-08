class Virus(object):
    '''Properties and attributes of the virus used in Simulation.'''

    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate

def test_virus_instantiation():
    virus = Virus("Tuberculosis", 0.32, 0.67)
    assert virus.name == "Tuberculosis"
    assert virus.repro_rate == 0.32
    assert virus.mortality_rate == 0.67
#Tests virus attributes
# virus = Virus("TB", 0.6, 0.3)
# print(virus.name)
# print(virus.mortality_rate)
# print(virus.repro_rate)
