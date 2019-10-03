# PROTIP: Write your tests before you solve each function, that way you can
    # test them one by one as you write your class. defining tests should be
    # as descriptive as possible as to make it clear what is wrong with your code.
import simulation
import logger
import person
import pytest
import random
import virus
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

def test_did_survive_infection():
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
    pass


def test_sick_person_instantiation():
    # Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # Create a Person object and give them the virus infection
    person = Person(3, False, virus)
    # TODO: complete your own assert statements that test
    # the values at each attribute
    # assert ...
    pass


def test_did_survive_infection():
    # TODO: Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # TODO: Create a Person object and give them the virus infection
    person = Person(4, False, virus)

    # Resolve whether the Person survives the infection or not
    survived = person.did_survive_infection()
    # Check if the Person survived or not
    if survived:
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


'''Qualifier tests! (tests edge cases and extra that don't fall in the above catagories)'''



''' 
# Example tests


def test_ability_instance():
    # Test instantiation without error
    big_strength = superheroes.Ability("Overwhelming Strength", 300)
    assert big_strength


def test_ability_name():
    # Test for Correct Name
    big_strength = superheroes.Ability("Overwhelming Strength", 300)
    assert big_strength.name == "Overwhelming Strength"


def test_ability_attack():
    # Test for correct attack value
    test_runs = 400
    big_strength = superheroes.Ability("Overwhelming Strength", 400)
    for _ in range(0, test_runs):
        attack = big_strength.attack()
        assert attack >= 0 and attack <= 400

# Test Weapons Class


def test_weapon_instance():
    big_stick = superheroes.Weapon("Overwhelming Stick", 200)
    assert "Weapon" in str(big_stick)


def test_weapon_attack():
    big_stick = superheroes.Weapon("Overwhelming Stick", 200)
    test_runs = 100
    for _ in range(0, test_runs):
        attack = big_stick.attack()
        assert attack <= 200 and attack >= 100


# Test Heroes Class
def test_hero_instance():
    Athena = superheroes.Hero("Athena")
    assert Athena


def test_hero_add_ability():
    big_strength = superheroes.Ability("Overwhelming Strength", 300)
    Athena = superheroes.Hero("Athena")
    assert len(Athena.abilities) == 0
    Athena.add_ability(big_strength)
    assert len(Athena.abilities) == 1
    # Check for correct type
    assert "Ability" in str(Athena.abilities[0])
    assert Athena.abilities[0].name == "Overwhelming Strength"


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


def test_hero_attack_ability():
    big_strength = superheroes.Ability("Overwhelming Strength", 30000)
    athena = superheroes.Hero("Athena")
    assert athena.attack() == 0
    athena.add_ability(big_strength)
    attack = athena.attack()
    assert attack <= 30000 and attack >= 0


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

def test_hero_ability_attack_standard_deviation():
    willow_waffle = superheroes.Hero("Willow Waffle")
    strength = random.randint(400, 30000)
    willow = superheroes.Ability("Willowness", strength)
    willow_waffle.add_ability(willow)
    attacks = list()
    total_attack = 0
    number_tests = 1000
    for _ in range(number_tests):
        cur_attack = willow_waffle.attack()
        attacks.append(cur_attack)
        total_attack += cur_attack
    mean = total_attack / number_tests
    
    # Get Square Deviations
    for index, value in enumerate(attacks):
        attacks[index] = math.pow(value - mean, 2)
    
    standard_dev = math.sqrt(sum(attacks) / len(attacks))
    print("Standard Deviation Cannot be 0.\nRandom Numbers not generated for attack.")
    assert standard_dev != 0.0
      
    
def test_hero_weapon_equip():
    sans = superheroes.Hero("Comic Sans")
    weapon = superheroes.Weapon("Garlic Hot Sauce", 400)
    sans.add_ability(weapon)
    assert len(sans.abilities) == 1
    assert sans.abilities[0].name == "Garlic Hot Sauce"

# This tests if the average of all attacks is correct.
# This test will faile if the random range of values is not correct. 
def test_hero_weapon_attack_mean_value():
    kkrunch = superheroes.Hero("Kaptain Krunch")
    strength = random.randint(10, 30000)
    min_attack = strength // 2
    big_strength = superheroes.Weapon("Sword of Whimsy", strength)
    kkrunch.add_ability(big_strength)
    calculated_mean = (strength - min_attack) // 2 + min_attack
    accepted_window = 400
    iterations = 6000

    sum_of_sqr = 0
    total_attack = 0

    for _ in range(iterations): 
        attack_value = kkrunch.attack()
        assert attack_value >= min_attack and attack_value <= strength
        total_attack += attack_value
        deviation = attack_value - calculated_mean
        sum_of_sqr += deviation * deviation

    actual_mean = total_attack / iterations
    print("Max Allowed Damage: {}".format(strength))
    print("Attacks Tested: {}".format(iterations))
    print("Mean -- calculated: {} | actual: {}".format(calculated_mean, actual_mean))
    print("Acceptable Min: {} | Acceptable Max: {}".format(actual_mean - accepted_window, actual_mean + accepted_window))
    print("Tested Result: {}".format(actual_mean))
    assert actual_mean <= calculated_mean + accepted_window 
    assert actual_mean >= calculated_mean - accepted_window

# This method uses statistics to check that a random value is given.
# This test will only fail if the same value is returned over the course of 1000 runs.
def test_hero_attack_standard_deviation():
    willow_waffle = superheroes.Hero("Willow Waffle")
    strength = random.randint(400, 30000)
    travel_agent = superheroes.Weapon("Travel Agents", strength)
    willow_waffle.add_ability(travel_agent)
    attacks = list()
    total_attack = 0
    number_tests = 1000
    for _ in range(number_tests):
        cur_attack = willow_waffle.attack()
        attacks.append(cur_attack)
        total_attack += cur_attack
    mean = total_attack / number_tests
    
    # Get Square Deviations
    for index, value in enumerate(attacks):
        attacks[index] = math.pow(value - mean, 2)
    
    standard_dev = math.sqrt(sum(attacks) / len(attacks))
    print("Random values not given. Please make sure you're not returning the same value every time.")
    assert standard_dev != 0.0

def test_hero_attack_weapon():
    big_strength = superheroes.Ability("Overwhelming Strength", 200)
    Athena = superheroes.Hero("Athena")
    Athena.add_ability(big_strength)
    test_runs = 100
    for _ in range(0, test_runs):
        attack = big_strength.attack()
        assert attack <= 200 and attack >= 0


def test_hero_multi_weapon_attack():
    strength = superheroes.Weapon("Overwhelming Strength", 200)
    sword_of_truth = superheroes.Weapon("Sword of Truth", 700)
    Athena = superheroes.Hero("Athena")
    Athena.add_ability(strength)
    Athena.add_ability(sword_of_truth)
    assert len(Athena.abilities) == 2

    test_runs = 100
    for _ in range(0, test_runs):
        attack = Athena.attack()
        assert attack <= 900 and attack >= 0


def test_hero_weapon_ability_attack():
    quickness = superheroes.Ability("Quickness", 1300)
    sword_of_truth = superheroes.Weapon("Sword of Truth", 700)
    Athena = superheroes.Hero("Athena")
    Athena.add_ability(quickness)
    Athena.add_ability(sword_of_truth)
    assert len(Athena.abilities) == 2
    attack_avg(Athena, 0, 2000)


def attack_avg(object, low, high):
    test_runs = 100
    for _ in range(0, test_runs):
        attack = object.attack()
        assert attack <= high and attack >= low

# Test Teams


def test_team_instance():
    team = superheroes.Team("One")
    assert team


def test_team_name():
    team = superheroes.Team("One")
    assert team.name == "One"


def test_team_hero():
    team = superheroes.Team("One")
    jodie = superheroes.Hero("Jodie Foster")
    team.add_hero(jodie)
    assert len(team.heroes) == 1
    assert team.heroes[0].name == "Jodie Foster"

#Failed - fixed by replacing str Jodie Foster with obj var jodie
def test_team_remove_hero():
    team = superheroes.Team("One")
    jodie = superheroes.Hero("Jodie Foster")
    team.add_hero(jodie)
    assert team.heroes[0].name == "Jodie Foster"
    team.remove_hero(jodie)
    assert len(team.heroes) == 0


def test_team_remove_unlisted():
    # Test that if no results found return 0
    team = superheroes.Team("One")
    jodie = superheroes.Hero("Jodie Foster")
    team.add_hero(jodie)
    code = team.remove_hero("Athena")
    assert code == 0


def test_team_remove_empty_list():
    team = superheroes.Team("One")
    assert team.remove_hero("Athena") == 0

#Failed -  fixed by changing in superheroes.py team.view_all_heroes hero in print to hero.name
def test_print_heroes():
    team = superheroes.Team("One")
    jodie = superheroes.Hero("Jodie Foster")
    team.add_hero(jodie)
    athena = superheroes.Hero("Athena")
    team.add_hero(athena)
    output_string = capture_console_output(team.view_all_heroes)

    assert "Jodie Foster" in output_string
    assert "Athena" in output_string '''