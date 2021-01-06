# Authors: Isaias Villalobos and Brian Rauh
import random
import copy
import math
import pandas as pd
import asteroids_exp

FARG = {'visual': False}

class Path():
    # Holds the moves made on this path, as well as the final number of
    # collisions and fuel remaining at its end.
    def __init__(self, initialState, moves):
        self.listMoves = moves
        state = initialState
        for move in moves:
            state = asteroids_exp.move(state, SA_Agent.MOVES[move[0]][0], 
                                       SA_Agent.MOVES[move[0]][1], move[1], 
                                       SA_Agent.window_width, 
                                       SA_Agent.window_height, FARG, None)
        self.fuel = state.ship.fuel
        self.collisions = state.num_collisions

class SA_Agent():
    MOVES = {'q': (-1, -1), 'w': (0, -1), 'e': (1, -1), 'a': (-1, 0),
             'd': (1, 0), 'z': (-1, 1), 'x': (0, 1), 'c': (1, 1), 's': (0, 0)}

    def __init__(self):
        """initialize environment and initial solution"""
        self.args = asteroids_exp.parse_args()
        self.args['visual'] = True
        self.env_state, self.window_width, self.window_height = asteroids_exp.init_asteroid_model(self.args)
        self.view = None

        # create the initial state
        initial_state, window_width, window_height = asteroids_exp.init_asteroid_model(self.args)

    # finish this method (10 points)
    def schedule(self, time):
        if time > 100:
            return 0  # output 0 for a temp
        else:
            return 1 / time

    """simulate a solution, return a reward value (10 points) """

    def returnReward(self, path):
        # If the path is in an illegal state (negative fuel, or too short 
        # a path), it is unfit. Otherwise, its value is inversely proportional
        # to the number of collisions along it. Short paths are rejected to
        # dissuade the program from soft locking with no moves.
        if path.fuel < 0:
            return 0
        elif len(path.listMoves) < self.env_state.ship.fuel:
            return 0
        else:
            return 1/path.collisions

    """choose a new random solution, via a local edit of current solution (10 points) """

    def successor(self, path, option = None):
        # Either adds a new move somewhere in the current path, removes an 
        # existing move, or changes out an existing move for a new move
        successor = copy.deepcopy(path)
        if option == None:
            option = random.randint(0,2)
        if option == 0:
            #add
            index = random.randint(0, len(successor.listMoves) + 1)
            successor.listMoves.insert(index, self.createMove())
        elif option == 1:
            #swap
            index = random.randint(0, len(path.listMoves))
            successor.listMoves.pop(index)
            successor.listMoves.insert(index, self.createMove())
        elif option == 2:
            #remove
            index = random.randint(0, len(path.listMoves))
            successor.listMoves.pop(index)
        return Path(self.env_state, successor.listMoves)
    
    def createMove():
        # Generates a random valid move to add to a path
        randAct = random.randint(0, 3)
        time = random.randrange(3, 90, 3)
        action = ''
        if randAct == 0:
            action = 's'
        elif randAct == 1:
            action = 'e'
        elif randAct == 2:
            action = 'd'
        elif randAct == 3:
            action = 'c'
        return (action, time)

    """determine whether to move to new state or remain in same place (10 points) """

    def shouldSwitchMoves(self, current, successor):
        # Compares the values in the reward function, and finds the deltaE
        return self.returnReward(successor) - self.returnReward(current)


a = SA_Agent()
"""run high-level simulated annealing algorithm (30 points)"""
temp = 0
current = Path(a.env_state, [])
for i in range(5):
    current = a.successor(current, 0)
while (True):  # for i to infinity
    T = a.schedule(temp)
    if T == 0:
        break
    else:
        successorNode = a.successor(current)
        deltaE = a.shouldSwitchMoves()
        if deltaE > 0:
            currentNode = successorNode
        else:
            if math.pow(math.e, deltaE / T) <= random.random:
                currentNode = successorNode

""" a.solution should be a list of ordered pairs of (directions, steps),
        just as in the asteroid_tree.py from hw4
"""
df = pd.DataFrame(current, columns=['direction', 'time'])
df.to_csv((".").join([a.args['in'].split(".")[0], "csv"]), index=False)
