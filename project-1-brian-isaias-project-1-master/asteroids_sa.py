# Authors: Isaias and Brian Rauh
import random
import copy
import math
import pandas as pd
import asteroids_exp

FARG = {'visual': False}

class Path():
    # Holds the moves made on this path, as well as the final number of
    # collisions and fuel remaining at its end.
    def __init__(self, agent, initialState, moves):
        self.listMoves = moves
        state = initialState
        self.distance = 0
        for move in moves:
            state = asteroids_exp.move(state, agent.MOVES[move[0]][0],
                                       agent.MOVES[move[0]][1], move[1],
                                       agent.window_width,
                                       agent.window_height, FARG, None)
            if move[0] != 's':
                self.distance += move[1]
        self.fuel = state.ship.fuel
        self.collisions = state.num_collisions

class SA_Agent():
    MOVES = {'q': (-1, -1), 'w': (0, -1), 'e': (1, -1), 'a': (-1, 0),
             'd': (1, 0), 'z': (-1, 1), 'x': (0, 1), 'c': (1, 1), 's': (0, 0)}
    window_width = 0
    window_height = 0

    def __init__(self, args):
        """initialize environment and initial solution"""
        self.args = {"in": args}
        self.args['visual'] = True
        self.env_state, self.window_width, self.window_height = asteroids_exp.init_asteroid_model(self.args)
        self.view = None


    # finish this method (10 points)
    def schedule(self, time):
        if time > 1000:
            return 0  # output 0 for a temp
        else:
            return 1 / time

    """simulate a solution, return a reward value (10 points) """

    def returnReward(self, path):
        # If the path is in an illegal state (negative fuel, or too short 
        # a path), it is unfit. Otherwise, its value is inversely proportional
        # to the number of collisions along it. Short paths are rejected to
        # dissuade the program from soft locking with no moves.
        if path.collisions == 0 and path.distance >= self.window_width:
            return 2
        elif path.collisions == 0:
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
        if option == 0 and path.fuel == 0:
            option = random.randint(1,2)
        if option == 0:
            #add
            index = random.randint(0, len(successor.listMoves))
            successor.listMoves.insert(index, self.createMove())
        elif option == 1:
            #swap
            index = random.randint(0, len(path.listMoves) - 1)
            successor.listMoves.pop(index)
            successor.listMoves.insert(index, self.createMove())
        elif option == 2:
            #remove
            index = random.randint(0, len(path.listMoves) - 1)
            successor.listMoves.pop(index)
        return Path(self, self.env_state, successor.listMoves)
    
    def createMove(self):
        # Generates a random valid move to add to a path
        randAct = random.randint(0, 3)
        time = random.randrange(1, self.window_width)
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

def main(args):

    a = SA_Agent(args)
    """run high-level simulated annealing algorithm (30 points)"""
    temp = 0  # not sure what unit the temperature should be
    current = Path(a,a.env_state, [])
    for i in range(current.fuel):
        current = a.successor(current, 0)
    while (True):  # for i to infinity
        temp += 1
        T = a.schedule(temp)
        if T == 0:
            break
        else:
            successorNode = a.successor(current)
            deltaE = a.shouldSwitchMoves(current, successorNode)
            if deltaE > 0:
                currentNode = successorNode
            else:
                if math.pow(math.e, deltaE / T) <= random.random():
                    currentNode = successorNode

    """ a.solution should be a list of ordered pairs of (directions, steps),
            just as in the asteroid_tree.py from hw4
    """
    print(current.listMoves)
    print(current.distance)
    print(a.window_width)
    print("reward = " + str(a.returnReward(current)))
    df = pd.DataFrame(current.listMoves, columns=['direction', 'time'])
    df.to_csv((".").join([a.args['in'].split(".")[0], "csv"]), index=False)
    
    return (current.fuel, current.listMoves)

if __name__ == '__main__':
    main("asteroid_game_2.json")