import tkinter as tk
import time
import json
import tkinter
import time
import argparse
import random
import copy
import math
import pandas as pd
import asteroids_exp
import pdb

POPULATION_SIZE = 10

"""
@param: screenWidth, a variable needed to create individuals that can contain
        some width of the screen
@env_state:
        This variable holds the fuel amount that will be used throughout the game
"""
def generatePopulation(screenWidth, env_state):
    solution = []
    for i in range(env_state.ship.fuel):
        distance = random.randint(1, screenWidth)
        direction = random.choice(['e', 's', 'd', 'c'])
        solution.append((distance, direction))
    return solution


class GA_Agent():

    """
    @args: the parameter represents a game string,
    which is a string that is the name of which game we are running
    """
    def __init__(self, args):
        self.args = {"in": args}
        self.args['visual'] = True
        self.env_state, self.window_width, self.window_height = asteroids_exp.init_asteroid_model(self.args)
        self.view = None

        # Create a list that will hold the population of individuals
        self.population = []
    """
    This funciton will create the original starting population.
    @return: a population that holds individuals    
    """
    def createPopulation(self):
        # Create the population of individuals that will be modified
        for i in range(POPULATION_SIZE):
            self.population.append(generatePopulation(self.window_width, self.env_state))
            # call the fitness function and start to filter out elements that are not useful to the population
            self.population = self.fitnessFunction(self.population)
        return self.population

    """
    This function will call a helper function, randomSelection(), to mutate a population 
    @return: Return a tuple that corresponds to the fuel and the path taken.
    @populationList: The population to mutate
    """
    def mutatePopulation(self, populationList):
        # Create a list that will hold a some members with mutations and orginal population members
        self.solution = []
        for i in range(len(populationList)):
            tupleList = populationList.__getitem__(i)
            mutatedChild = self.randomSelection(self.window_width, tupleList)
            self.solution.append(mutatedChild)

        return self.solution

    """
    The purpose of the randomSelection is to begin mutating the population
    by introducing randomness into the population. 
    @return: Return a tuple that corresponds to the fuel and the path taken.
    @param: A window width, an individual will need to select a value in that range
    @tupleList: The population to mutate
    """
    def randomSelection(self, window_width, tupleList):
        # Mutate some members in population to add genetic variation
        newTupleList = []
        for tuple in tupleList:
            newTuple = tuple
            if random.random() > 0.5:
                x, y = tuple
                if y == "s":
                    elementOne = random.randint(1, window_width)
                    newTuple = (elementOne, 's')
                else:
                    elementTwo = random.choice(['e', 'd', 'c'])
                    newTuple = (x, elementTwo)

            newTupleList.append(newTuple)
        return newTupleList

    """
    The purpose of the fitness function is to choose an individual that is the
    best in terms of the which individuals can reach the window_width.
    @return: Return a tuple that corresponds to the fuel and the path taken.
    """
    def fitnessFunction(self, population):
        # best individual would be an element that has
        # is able to reach  window screen width
        filteredList = []
        for tuple in population:
            cumSumDistance = 0
            for el in tuple:
                # print("element is ", el)
                distance, direction = el
                cumSumDistance += distance
            if cumSumDistance > self.window_width:
                cumSumDistance = 0
                continue
            elif cumSumDistance == self.window_width:
                filteredList.append(tuple)
        return filteredList

"""
The main program that will run the Genetic Algorithm high level algorithm
@return: Return a tuple that corresponds to the fuel and the path taken.
"""
def main(args):
    # instance of Genetic Algorithm Agent
    agent = GA_Agent(args)

    # The high level overview of the algorithm
    while (True):
        newPopulation = agent.createPopulation()
        mutatedPopulation = agent.mutatePopulation(newPopulation)
        population = mutatedPopulation
        if len(population) > 0:
            return (0, agent.solution)
    # The dataframe information
    df = pd.DataFrame(agent.solution, columns=['direction', 'time'])
    df.to_csv((".").join([agent.args['in'].split(".")[0], "csv"]), index=False)
    

if __name__ == '__main__':
    main("asteroid_game_6.json")
