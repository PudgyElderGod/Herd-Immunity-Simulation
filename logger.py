#---------Logger Class----------#
class Logger(object):
    ''' Utility class responsible for logging all interactions during the simulation. '''
    def __init__(self, file_name):
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        '''
        The simulation class should use this method immediately to log the specific
        parameters of the simulation as the first line of the file.
        '''
        metadata = (f'{pop_size}, {vacc_percentage}, {virus_name}, {mortality_rate}, {basic_repro_num}\n')

        data_file = open(self.file_name, 'w')
        data_file.write(metadata)
        data_file.close()

    def log_interaction(self, person, random_person, random_person_sick=None,
                        random_person_vacc=None, did_infect=None):
        '''
        The Simulation object should use this method to log every interaction
        a sick person has during each time step.
        The format of the log should be: "{person.ID} infects {random_person.ID} \n"
        or the other edge cases:
            "{person.ID} didn't infect {random_person.ID} because {'vaccinated' or 'already sick'} \n"
        '''
        log = ''
        data_file = open(self.file_name, 'a')
        if random_person_sick:
            if did_infect:
                log += f'{person._id} has infected {random_person._id}\n'
            else:
                log +=(f"{person._id} failed to infect {random_person._id}) " "because they are already infected\n")
        else:
            if random_person_vacc:
                log += (f"{person._id} has failed to infect {random_person._id}" " because they were vaccinated\n")

        data_file.write(log)
        data_file.close()

    def log_infection_survival(self, person, did_die_from_infection):
        ''' The Simulation object uses this method to log the results of every
        call of a Person object's .resolve_infection() method.
        The format of the log should be:
            "{person.ID} died from infection\n" or "{person.ID} survived infection.\n"
        '''
        with open(self.file_name, mode = 'a') as file:
            file.write('Infection Survival: ')

            if did_die_from_infection:
                status = f'{person._id} has perished.\n'

            else:
                status = f'{person._id} has survived.\n'
            file.write(status)
            file.close()


    def log_time_step(self, time_step_number):
        ''' STRETCH CHALLENGE DETAILS:
        If you choose to extend this method, the format of the summary statistics logged
        are up to you.
        At minimum, it should contain:
            The number of people that were infected during this specific time step.
            The number of people that died on this specific time step.
            The total number of people infected in the population, including the newly infected
            The total number of dead, including those that died during this time step.
        The format of this log should be:
            "Time step {time_step_number} ended, beginning {time_step_number + 1}\n"
        '''
        # TODO: Finish this method. This method should log when a time step ends, and a
        # new one begins.
        # NOTE: Here is an opportunity for a stretch challenge!
        with open(self.file_name, mode = 'a') as file:
            file.write(f'Time step {time_step_number} ended, beginning {time_step_number+1}\n')


log = Logger('metadata')
