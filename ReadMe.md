# Herd Immunity Simulation by Aloysha 'Thom' d'Olanie & Anthony Sean Protho
# Virus Name: "Tuberculosis" Moratlity Rate: "67%" Repo Rate: "5.6(or 32.94%)"

We created a basic simulation of herd immunity by modeling how a virus moves through a population where some (but not all) of a population is vaccinated against this virus.

* During every time step of the simulation, **every sick person** should randomly interact with **100 other people** in the population. The chance of a sick person infecting a person that they interact with is the virus's reproductive rate.  Example: if a virus has a reproductive rate of 15, then, on average, a sick person should infect 15 of the 100 people they interact with during that time step.

### Rules

1. A sick person only has a chance at infecting healthy, **unvaccinated** people they encounter.  
2. An infected person cannot infect a vaccinated person.  This still counts as an interaction.  
3. An infected person cannot infect someone that is already infected.  This still counts as an interaction.
4. At the end of a time step, an infected person will either die of the infection or get better.  The chance they will die is the percentage chance stored in mortality_rate.  
5. For simplicity's sake, if the person does not die, we will consider them immune to the virus and change is_vaccinated to True when this happens.  
6. Dead people can no longer be infected, either.  Any time an individual dies, we should also change their .infected attribute to False.  
7. All state changes for a person should occur at the **end** of a time step, after all infected persons have finished all of their interactions.  
8. During the interactions, make note of any new individuals infected on this turn.  After the interactions are over, we will change the .infected attribute of all newly infected individuals to True.  1. Resolve the states of all individuals that started the turn infected by determining if they die or survive the infection, and change the appropriate attributes.  
9. The simulation should output a logfile that contains a record of every interaction that occurred during the simulation.  We will use this logfile to determine final statistics and answer questions about the simulation.

## Running the Program

The program is designed to be run from the command line.  You can do this by running
`python3 simulation.py` followed by the command line arguments in the following order,
separated by spaces:
 {population size} {vacc_percentage} {virus_name} {mortality_rate} {repro_rate} {optional: number of people initially infected (default is 1)}

 Here's an example:
 * Population Size: 100,000
 * Vaccination Percentage: 90%
 * Virus Name: Ebola
 * Mortality Rate: 70%
 * Reproduction Rate: 25%
 * People Initially Infected: 10

 Then I would type: <br>
 `python3 simulation.py 100000 0.90 Ebola 0.70 0.25 10` in the terminal.

## Basic Structure

When you run `simulation.py` with the corresponding command-line arguments necessary for a simulation, a simulation object is created.  This simulation object then calls the `.run()` method.  This method should continually check if the simulation needs to run another step using a helper method contained in the class, and then call `.time_step()` if the simulation has not ended yet.  Within the `time_step()` method, you'll find all the logic necessary for actually simulating everything--that is, once you write it.  As is, the file just contains a bunch of method stubs, as well as numerous comments for explaining what you need to do to get everything working.  

**Your repo should contain:**
  * Completed classes for `logger.py`, `simulation.py`, and `person.py`.
  * The addition of at least 2 additional tests to the `virus.py` file.
  * The addition of at least 3 additional tests to the `person.py` file.
  * At least 1 log file generated from running your simulation.
  * `simulation_test.py` file should be created that allows for testing the simulation.
  * `logger_test.py` file should be created that allows for the testing of the logger class.
  * Answers to the questions asked in `answers.txt`.

### Stretch Challenges

  * Create a Visualizer class that can spit out visualizations of the spread of the virus based on the log files of a simulation.  HINT: You'll want to use Matplotlib for visualization stuff, because its easy to use and generally awesome at this sort of thing.  You may also want to consider using a library like Pandas for organizing and cleaning your data in a more professional way, especially if you want to visualize answers to more complex questions.  Matplotlib and Pandas play very nicely together! (Difficulty Level: Medium)
  * Extending functionality so that we can test the spread of multiple viruses through a given population at the same time. (Difficulty Level: Hard)
  