# PROTIP: Write your tests before you solve each function, that way you can
    # test them one by one as you write your class. defining tests should be
    # as descriptive as possible as to make it clear what is wrong with your code.
from simulation import Simulation
from logger import Logger
from person import Person
from virus import Virus
import pytest
import random
import math
import sys
import io


# Helper Function
def capture_console_output(function_body):
    # _io.StringIO object
    string_io = io.StringIO()
    sys.stdout = string_io
    function_body()
    sys.stdout = sys.__stdout__
    return string_io.getvalue()


'''Logger Class Tests! (logger.py)'''
 # TODO: Write a test suite for Logger class to make sure each method is working
    # as expected.

def test_file_name_value():
    pass

def test_writen_metadata():
    pass

def test_log_interaction():
    pass

def test_log_infection_survival(self, person, did_die_from_infection):
    pass

def test_log_time_step():
    pass


'''Person Class Tests! (person.py)''' 
def test_is_alive():
    pass

def test_infection_state():
    pass


''' These are simple tests to ensure that you are instantiating your Person class correctly. '''
def test_vacc_person_instantiation():
    # create some people to test if our init method works as expected
    person = Person(1, True)
    assert person._id == 1
    assert person.is_alive is True
    assert person.is_vaccinated is True
    assert person.infection is None


def test_not_vacc_person_instantiation():
    person = Person(2, False)
    # TODO: complete your own assert statements that test
    # the values at each attribute
    # assert ...
    assert person == person # bad test, just gets rid of warning
    pass


def test_sick_person_instantiation():
    # Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # Create a Person object and give them the virus infection
    person = Person(3, False, virus)
    # TODO: complete your own assert statements that test
    # the values at each attribute
    # assert ...
    assert person == person # bad test, just gets rid of warning
    pass


def test_did_survive_infection():
    # TODO: Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # TODO: Create a Person object and give them the virus infection
    person = Person(4, False, virus)

    # Resolve whether the Person survives the infection or not
    #suvived = person.did_survive_infection()
    # Check if the Person survived or not *changed survived directly into person.did_survive_infection()
        #as to fix bugs, however this is not best practice and should be reverted back when method
        #has been made functional
    if person.did_survive_infection():
        assert person.is_alive is True
        # TODO: Write your own assert statements that test
        # the values of each attribute for a Person who survived
        # assert ...
    else:
        assert person.is_alive is False
        # TODO: Write your own assert statements that test
        # the values of each attribute for a Person who did not survive
        # assert ...
        pass


'''Simulation Class Tests! (simulation.py)'''
def test_logger():
    pass

def test_population():
    pass

def test_pop_size():
    pass

def test_next_person_id():
    pass

def test_virus():
    pass

def test_initial_infected():
    pass

def test_total_infected():
    pass

def test_current_infected():
    pass

def test_vacc_percentage():
    pass

def test_total_dead():
    pass

def test_file_name():
    pass

def test_newly_infected():
    pass

def test_create_population():
    pass

def test_simulation_should_continue():
    pass

def test_run():
    pass

def test_time_step():
    pass

def test_interaction():
    pass

def test_infect_newly_infected():
    pass


'''Virus Class Tests! (virus.py)'''
def test_virus_instantiation():
    #TODO: Create your own test that models the virus you are working with
    '''Check to make sure that the virus instantiator is working.'''
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3


''' Example tests!! '''
'''
def test_hero_instance():
    Athena = superheroes.Hero("Athena")
    assert Athena

def test_ability_instance():
    # Test instantiation without error
    big_strength = superheroes.Ability("Overwhelming Strength", 300)
    assert big_strength

def test_weapon_attack():
    big_stick = superheroes.Weapon("Overwhelming Stick", 200)
    test_runs = 100
    for _ in range(0, test_runs):
        attack = big_stick.attack()
        assert attack <= 200 and attack >= 100


def test_hero_add_multi_ability():
    big_strength = superheroes.Ability("Overwhelming Strength", 300)
    speed = superheroes.Ability("Lightning Speed", 500)
    Athena = superheroes.Hero("Athena")
    assert len(Athena.abilities) == 0
    Athena.add_ability(big_strength)
    assert len(Athena.abilities) == 1
    Athena.add_ability(speed)
    assert len(Athena.abilities) == 2
    # Check for correct type
    assert "Ability" in str(Athena.abilities[0])
    assert Athena.abilities[0].name == "Overwhelming Strength"


def test_hero_ability_attack_mean_value():
    athena = superheroes.Hero("Athena")
    strength = random.randint(10, 30000)
    big_strength = superheroes.Ability("Overwhelming Strength", strength)
    athena.add_ability(big_strength)
    calculated_mean = strength // 2
    iterations = 6000
    accepted_window = 400

    total_attack = 0

    for _ in range(iterations): 
        attack_value = athena.attack()
        assert attack_value >= 0 and attack_value <= strength
        total_attack += attack_value

    actual_mean = total_attack / iterations
    print("Max Allowed Damage: {}".format(strength))
    print("Attacks Tested: {}".format(iterations))
    print("Mean -- calculated: {} | actual: {}".format(calculated_mean, actual_mean))
    print("Acceptable Distance from Mean: {} | Average distance from mean: {}".format(accepted_window, abs(calculated_mean - actual_mean)))
    print("Acceptable min attack: {} | Acceptable max attack: {}".format(actual_mean - accepted_window, actual_mean + accepted_window))
    assert actual_mean <= calculated_mean + accepted_window and actual_mean >= calculated_mean - accepted_window
'''