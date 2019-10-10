import random, sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus

class Simulation(object):
    ''' Main class that will run the herd immunity simulation program.
    Expects initialization parameters passed as command line arguments when file is run.

    Simulates the spread of a virus through a given population.  The percentage of the
    population that are vaccinated, the size of the population, and the amount of initially
    infected people in a population are all variables that can be set when the program is run.
    '''
    def __init__(self, pop_size, vacc_percentage, initial_infected, virus):
        ''' Logger object logger records all events during the simulation.
        Population represents all Persons in the population.
        The next_person_id is the next available id for all created Persons,
        and should have a unique _id value.
        The vaccination percentage represents the total percentage of population
        vaccinated at the start of the simulation.
        You will need to keep track of the number of people currently infected with the disease.
        The total infected people is the running total that have been infected since the
        simulation began, including the currently infected people who died.
        You will also need to keep track of the number of people that have died as a result
        of the infection.

        All arguments will be passed as command-line arguments when the file is run.
        HINT: Look in the if __name__ == "__main__" function at the bottom.
        '''     
        self.population = [] # List of Person objects
        self.pop_size = pop_size # Int
        self.next_person_id = 0 # Int
        self.virus = virus # Virus object
        self.initial_infected = initial_infected # Int
        self.total_infected = 0 # Int
        self.current_infected = 0 # Int
        self.vacc_percentage = vacc_percentage # float between 0 and 1
        self.total_dead = 0 # Int
        self.file_name = "logs/{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(virus_name, pop_size, vacc_percentage, initial_infected)
        self.logger = Logger(self.file_name)
        self.newly_infected = []
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate)

    def _create_population(self, initial_infected):
        '''This method will create the initial population.
            Args:
                initial_infected (int): The number of infected people that the simulation
                will begin with.

            Returns:
                list: A list of Person objects.
        '''    
        # TODO: Look over logic, Make Tests!!
        vacc = int(self.pop_size * self.vacc_percentage)
        infec = self.initial_infected + vacc
        for i in range(0, vacc):
            person = Person(i, True, None)
            self.population.append(person)
        for i in range(vacc, infec):
            person = Person(i, False, virus)
            self.population.append(person)
        for i in range(infec, self.pop_size):
            person = Person(i, False)
            self.population.append(person)

        return self.population

    def _simulation_should_continue(self):
        ''' The simulation should only end if the entire population is dead
        or everyone is vaccinated, or if no one is infected

            Returns:
                bool: True for simulation should continue, False if it should end.
        '''
        for person in self.population:
            if person.is_alive == True and person.infection == self.virus:
                return True

        return False

    def run(self):
        ''' This method should run the simulation until all requirements for ending
        the simulation are met.
        '''
        self._create_population(self.initial_infected)
        time_step_counter = 0

        while self._simulation_should_continue():
            time_step_counter += 1
            self.time_step()
            self.logger.log_time_step(time_step_counter)
        print('The simulation has ended after {} turns.'.format(time_step_counter))

    def time_step(self):
        ''' This method should contain all the logic for computing one time step
        in the simulation.

        This includes:
            1. 100 total interactions with a randon person for each infected person
                in the population
            2. If the person is dead, grab another random person from the population.
                Since we don't interact with dead people, this does not count as an interaction.
            3. Otherwise call simulation.interaction(person, random_person) and
                increment interaction counter by 1.
            '''
        inf_list = []
        for infected in self.population:
            if infected.infection == self.virus and infected.is_alive:
                inf_list.append(infected)

        for infected in inf_list:
            for interaction in range(100):
                rand_person_index = random.randint(0, self.pop_size-1)
                rand_person = self.population[rand_person_index]
                if rand_person.is_alive == False:
                    interaction -= 1
                else:
                    self.interaction(infected, rand_person)

        for infected in inf_list:
            did_die = not infected.did_survive_infection()
            self.logger.log_infection_survival(infected, did_die)
        
        self._infect_newly_infected()

    def interaction(self, person, random_person):
        '''This method should be called any time two living people are selected for an
        interaction. It assumes that only living people are passed in as parameters.

        Args:
            person1 (person): The initial infected person
            random_person (person): The person that person1 interacts with.
        '''
        # Assert statements are included to make sure that only living people are passed
        # in as params
        assert person.is_alive == True
        assert random_person.is_alive == True

        if random_person.is_vaccinated == True:
            self.logger.log_interaction(person, random_person, False, True, False)
        elif random_person.infection is not None:
            self.logger.log_interaction(person, random_person, True, False, False)
        elif random_person.infection == None and random_person.is_vaccinated == False:
            chance = random.random()
            if chance < person.infection.repro_rate:
                self.newly_infected.append(random_person)
                self.logger.log_interaction(person, random_person, True, False, True)
        

    def _infect_newly_infected(self):
        ''' This method should iterate through the list of ._id stored in self.newly_infected
        and update each Person object with the disease. '''
        for infected in self.newly_infected:
            infected.infection = self.virus
        self.newly_infected = []


if __name__ == "__main__":
    params = sys.argv[1:]
    pop_size = int(params[0])
    vacc_percentage = float(params[1])

    virus_name = str(params[2])
    repro_num = float(params[3])
    mortality_rate = float(params[4])

    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1
    virus = Virus(virus_name, repro_num, mortality_rate)
    sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)
    sim.run()
#Thank you David for all the help!