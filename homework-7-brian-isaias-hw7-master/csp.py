# Authors: Brian Rauh and Isaias Villabos

import pandas as pd
import sys
import copy
"""
Read two input arguments: the size of the board (as n) and the 
number of rooks and bishops each (as k) [5 points]
"""

"""
At every level of the search tree: iterate over each constraint with
which the variable assigned at that level shares a constraint
(these may be hard-coded, but you should indicate where via a comment 
where you check the constraints) and use the known_values attributes to perform 
forward checking. [10 points]
"""

# Add minimum remaining values heuristic [10 points]

def checkMRV(piece):
    """
    The 2/x is hardcoded with the idea that if there is only one place to put
    a given piece, it will always get priority, regardless of rook or bishop,
    but will otherwise allow rooks to take precedence in placement over bishops.
    
    If the piece has no valid placements, -1 is returned to signify it's reset time
    """
    options = len(piece.known_values)
    if options > 0:
        return 2/options
    else:
        return -1

# Add least constraining values heuristic [10 points]

def checkLCV(loc, p_type, r_dom, b_dom):
    """
    Counts how many values a given placement will remove from the domains, and
    returns a value inversely proportional. Currently counts removing a square
    that a bishop or rook could do on twice, but given that results are
    relative anyway, this is not a major issue.
    
    Todo: Make counting more efficient (will also stop double-counting)
    """
    count = 0
    if p_type == "R":
        for pos in r_dom:
            if loc[0] == pos[0]:
                count += 1
            elif loc[1] == pos[1]:
                count += 1
        for pos in b_dom:
            if loc[0] == pos[0]:
                count += 1
            elif loc[1] == pos[1]:
                count += 1
    elif p_type == "B":
        for pos in r_dom:
            if loc[0] - loc[1] == pos[0] - pos[1]:
                count += 1
            elif loc[0] + loc[1] == pos[0] + pos[1]:
                count += 1
        for pos in b_dom:
            if loc[0] - loc[1] == pos[0] - pos[1]:
                count += 1
            elif loc[0] + loc[1] == pos[0] + pos[1]:
                count += 1
    """
    Returns 1/count because the exact value doesn't matter, just that it's
    inversely proportional to count
    """
    if count > 0:
        return 1/count
    else:
        return 0

# Add an arc consistency heuristic [5 points]

def checkAC(loc, b_type, values):
    """
    Our arc consistency is the inverse of the forward-checking. While foward
    checking removes squares on both boards the same, but the squares removed
    depend on the piece (i.e. which squares the piece threatens), arc
    consistency doesn't care what the piece is, just where new pieces of a 
    given type need to avoid being placed because they would threaten the
    just-placed piece.
    """
    to_remove = []
    if b_type == "R":
        for pos in values:
            if loc[0] == pos[0]:
                to_remove.append(pos)
            elif loc[1] == pos[1]:
                to_remove.append(pos)
    elif b_type == "B":
        for pos in values:
            if loc[0] - loc[1] == pos[0] - pos[1]:
                to_remove.append(pos)
            elif loc[0] + loc[1] == pos[0] + pos[1]:
                to_remove.append(pos)
    for el in to_remove:
        values.remove(el)

"""
Each variable object must have as an attribute (called known_values) a set containing 
all of the possible values in the domain when the object is 
initialized [5 points]
"""
class Piece():
    def __init__(self, values):
        self.known_values = copy.deepcopy(values)
        self.assigned = False
        self.position = None
        
# Variable object should also have a boolean variable called assigned [5 points]
    def assign(self):
        self.assigned = True
        
    def getValues(self):
        return self.known_values
    
    def setValues(self, values):
        self.known_values = values
    
    def getPos(self):
        return self.position
    
    def setPos(self, pos):
        self.position = pos

def chooseNextPiece(pieces):
    """
    Chooses next piece based on the MRV heuristic, with a bias towards rooks
    """
    nextPiece = ""
    nextVal = 0
    assigned = 0
    for key in pieces:
        if pieces[key].assigned:
            assigned += 1
            continue
        if key[0] == "R":
            thisVal = 1
        else:
            thisVal = 0
        options = checkMRV(pieces[key])
        if options == -1:
            return ""
        thisVal += options
        if thisVal > nextVal:
            nextVal = thisVal
            nextPiece = key
    if assigned == len(pieces):
        return "success"
    return nextPiece

def forwardCheck(loc, p_type, values):
    """
    Takes all the squares the newly placed piece threatens out of the set of
    viable placements.
    """
    to_remove = []
    if p_type == "R":
        for pos in values:
            if loc[0] == pos[0]:
                to_remove.append(pos)
            elif loc[1] == pos[1]:
                to_remove.append(pos)
    elif p_type == "B":
        for pos in values:
            if loc[0] - loc[1] == pos[0] - pos[1]:
                to_remove.append(pos)
            elif loc[0] + loc[1] == pos[0] + pos[1]:
                to_remove.append(pos)
    for el in to_remove:
        values.remove(el)

def make_move(pieces, b_dom, r_dom, move, p_type):
    """
    Updates the board (for display purposes) as well as the domains of each of
    the variables. Note that due to the way forward-checking and arc 
    consistency coincide, there is no need to run the arc consistency check on
    the rook domain when a rook is placed, and vise versa for bishops. This is
    because the forward checking will already have eliminated the squares arc
    consistency would find.
    """
    forwardCheck(move, p_type, b_dom)
    forwardCheck(move, p_type, r_dom)
    checkAC(move, "B", b_dom)
    checkAC(move, "R", r_dom)
    for key in pieces:
        if key[0] == "B":
            pieces[key].known_values = b_dom
        else:
            pieces[key].known_values = r_dom

# Implement basic backtracking algorithm [35 points]
def backTrack(pieces, b_dom, r_dom):
    """
    Way too much deep copying here, but it still gets the bigger one done in a
    handful of seconds, so I'm not sweating it.
    """
    piece = chooseNextPiece(pieces)
    if piece == "":
        return None
    if piece == "success":
        return pieces
    p_type = piece[0]
    pieces[piece].known_values.sort(key=lambda x : checkLCV(x, p_type, r_dom, b_dom))
    
    for i in range(len(pieces[piece].known_values)):
        move = pieces[piece].known_values[i]
        pieces_c = copy.deepcopy(pieces)
        b_dom_c = copy.deepcopy(b_dom)
        r_dom_c = copy.deepcopy(r_dom)
        pieces_c[piece].assign()
        pieces_c[piece].setPos(move)
        make_move(pieces_c, b_dom_c, r_dom_c, move, p_type)
        solution = backTrack(pieces_c, b_dom_c, r_dom_c)
        if solution:
            return solution

def main():
    """
    Takes in args, initializes the board, pieces, and domains. Also converts
    results into a dataframe and writes it to a csv.
    """
    n = int(sys.argv[1])
    k = int(sys.argv[2])

    values = []
    for i in range(n):
        for j in range(n):
            values.append((i, j))

    pieces = {}
    for i in range(k):
        pieces["Rook" + str(i)] = Piece(values)
    for i in range(k):
        pieces["Bishop" + str(i)] = Piece(values)
    
    pieces = backTrack(pieces, values, copy.deepcopy(values))

    solution = []
    for key, value in pieces.items():
        solution.append([key, value.getPos()])
    """
    Output your solution into a file called "csp_n_k.csv," a csv file 
    where n and k are the input arguments, and the headers are "name" and "value."
    There should be one line per variable. You can name your variables 
    however you like, but the convention should be obvious to the grader.
    5 points per output file.
    """
    df = pd.DataFrame(solution, columns=["Name", "Value"])
    df.to_csv("csp_" + str(n) + "_" + str(k) + ".csv")

main()

#Good work!