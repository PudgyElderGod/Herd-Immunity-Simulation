# Herd Immunity Simulation by Aloysha 'Thom' d'Olanie & Anthony Sean Protho
# Virus Name: "Tuberculosis" Moratlity Rate: "67%" Repo Rate: "5.6(or 32.94%)"

We're going to create a basic simulation of herd immunity by modeling how a virus moves through a population where some (but not all) of a population is vaccinated against this virus.

## Goals

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

 Let's look at an example:
 * Population Size: 100,000
 * Vaccination Percentage: 90%
 * Virus Name: Ebola
 * Mortality Rate: 70%
 * Reproduction Rate: 25%
 * People Initially Infected: 10

 Then I would type: <br>
 `python3 simulation.py 100000 0.90 Ebola 0.70 0.25 10` in the terminal.

## Basic Structure

The program consists of 4 classes: `Person`, `Virus`, `Simulation`, and `Logger`.

* `Simulation`: Highest level of abstraction. The main class that runs the entire simulation.
* `Person`: Represents the people that make up the population that the virus is spreading through.
* `Virus`: Models the properties of the virus we wish to simulate.
* `Logger`: A helper class for logging all events that happen in the simulation.

When you run `simulation.py` with the corresponding command-line arguments necessary for a simulation, a simulation object is created.  This simulation object then calls the `.run()` method.  This method should continually check if the simulation needs to run another step using a helper method contained in the class, and then call `.time_step()` if the simulation has not ended yet.  Within the `time_step()` method, you'll find all the logic necessary for actually simulating everything--that is, once you write it.  As is, the file just contains a bunch of method stubs, as well as numerous comments for explaining what you need to do to get everything working.  

## Tips for Success

First, take a look at each of the files.  Get a feel for the methods and attributes in each.  Feel overwhelmed? Don't panic.  Instead, get out a piece of paper or a whiteboard and try to diagram what needs to happen and when using each of the objects and methods. Draw out the data flow.

*_If you don't understand something, talk to your classmates and ask for help!_*

Ask your classmates and teachers for clarification/help/code reviews as needed, or drop in to tutoring hours. Share your questions and insights in the course Slack channel, or book some time to get help from Justin and Phyllis, the course teaching assistants.
Collaboration is encouraged, but be sure that you typed in all the code yourself and the final project is your own!

*Found a bug or a problem? Contact the course instructors or teaching assistants!*

## Project Completion

For this project to be considered complete, you need to add your repo link to the course tracker. Please do not change the random seed set in the Simulation class! It is currently set to 42, and we will use this to double check that your simulation works and spits out the expected results.

**Your repo should contain:**
  * Completed classes for `logger.py`, `simulation.py`, and `person.py`.
  * The addition of at least 2 additional tests to the `virus.py` file.
  * The addition of at least 3 additional tests to the `person.py` file.
  * At least 1 log file generated from running your simulation.
  * `simulation_test.py` file should be created that allows for testing the simulation.
  * `logger_test.py` file should be created that allows for the testing of the logger class.
  * Answers to the questions asked in `answers.txt`.

### Stretch Challenges

You'll find some of the smaller, individual stretch challenges contained with the comments of the code on the logger class.  Other stretch challenges include:

  * Create a Visualizer class that can spit out visualizations of the spread of the virus based on the log files of a simulation.  HINT: You'll want to use Matplotlib for visualization stuff, because its easy to use and generally awesome at this sort of thing.  You may also want to consider using a library like Pandas for organizing and cleaning your data in a more professional way, especially if you want to visualize answers to more complex questions.  Matplotlib and Pandas play very nicely together! (Difficulty Level: Medium)
  * Extending functionality so that we can test the spread of multiple viruses through a given population at the same time. (Difficulty Level: Hard)
  
