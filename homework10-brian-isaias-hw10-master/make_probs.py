"""
Authors: Brian Rauh and Isaias Villabos
"""

import pandas as pd

def count_occurrences(data, g, l, r, s, e, o, t,):
    df = data.query('G == ' + str(g) +
                    '& L == ' + str(l) +
                    '& R == ' + str(r) +
                    '& S == ' + str(s) +
                    '& E == ' + str(e) +
                    '& O == ' + str(o) +
                    '& T == ' + str(t))
    return len(df.index) / 10000

def problem_one(data):
    df = data.query('S == True & T == True')
    sub_df = data.query('S == True & T == True & G == True')
    
    print(sub_df.sum(axis = 0)[8] / df.sum(axis = 0)[8])

def problem_two(data):
    df = data.query('E == False')
    sub_df = data.query('E == False & R == True & S == True')
    
    print(sub_df.sum(axis = 0)[8] / df.sum(axis = 0)[8])
    
def problem_three(data):
    df = data.query('T == True')
    sub_df = data.query('T == True & O == True & L == False & G == False')

    print((df.sum(axis = 0)[8] - sub_df.sum(axis = 0)[8]) / df.sum(axis = 0)[8])
    
def problem_four(data):
    df = data.query('S == True & O == True & L == True')
    sub_df = data.query('S == True & O == True & L == True & R == False & E == True')
    
    print(sub_df.sum(axis = 0)[8] / df.sum(axis = 0)[8])

def main():
    data = pd.read_csv('graph_data_bool.csv')
    data_two = pd.read_csv('probs.csv')
    probs = []
    for i in range(0,2):
        if(i == 0):
            g = True
        else:
            g = False
        for j in range(0,2):
            if(j == 0):
                l = True
            else:
                l = False
            for w in range(0,2):
                if(w == 0):
                    r = True
                else:
                    r = False
                for q in range(0,2):
                    if(q == 0):
                        s = True
                    else:
                        s = False
                    for x in range(0,2):
                        if(x == 0):
                            e = True
                        else:
                            e = False
                        for m in range(0,2):
                            if(m == 0):
                                o = True
                            else:
                                o = False
                            for n in range(0,2):
                                if(n == 0):
                                    t = True
                                else:
                                    t = False
                                prob = count_occurrences(data, g, l, r, s, e, o, t)
                                probs.append([g,l,r,s,e,o,t,prob])
    probabilities = pd.DataFrame(probs, columns = ['G','L','R','S','E','O','T','P'])
    probabilities.to_csv('probs.csv')
    
    # These print out the answers to the various homework problems.
    problem_one(probabilities)
    problem_two(probabilities)
    problem_three(probabilities)
    problem_four(probabilities)
    

if __name__ == '__main__':
    main()