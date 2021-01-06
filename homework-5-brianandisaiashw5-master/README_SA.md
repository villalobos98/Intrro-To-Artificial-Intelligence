#Isaias Villalobos and Brian Rauh

##How it works:
Basically the code that was changed was inside the asteroids_sa file which had to be finshed.
In order to finish the method, we had to construct 4 different helper functions.
The first was the schedule function which was a function of a time, and it output a value
which was a temperature, the function needed to be chosen so that the the highest the input value
was given to the function, the lower the the value of the ouput. 1/x, matched perfectly was we needed to do.
The next function was the successor() function which either makes a new move somwher eint hecurrent path removes an existing move or changes out an existing move for a new move.

##Strategy:
The base algorithm is the same as textbook simulated annealing. Our reward function penalizes a path for every collision it has, and outright rejects illegal paths. Illegal paths are those with negative fuel or a too-short path (to prevent the algorithm from removing to 0 moves and getting a "perfect" score. Successors are randomly determined, with local changes made by either adding, removing, or "swapping" (removing, then adding in the same place) a random move in the path. 

##How to run code:
As expected in README.md

##Some Issues we ran into:
- Not fully complete
- How to run the initial code
- Problem space was daunting
- Known bugs: Program can softlock if waiting at location where no asteroids fall, as 0 collisions = max reward function
