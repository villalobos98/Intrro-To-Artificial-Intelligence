## Homework 4
# Brian Rauh
# Isaias Villalobos


How to Run:
-   The code should be run with the my_asteroids_tree.py file in place of the asteroids_tree.py file, using the following command line arguments:
python3 my_asteroid_tree.py -i [ Enter JSON of game]
This creates the CSVs like the original version did. 


Strategy Used:
-   The overall strategy and BFS algorithm were not changed, and our modifications were kept contained to the expand() function. The changes made include:
Removing s as a valid option when only one fuel remained. Using s in such a scenario would leave the ship dead in space with no fuel to resume moving, which creates unnecessary nodes and wastes time.
Expanding time windows while introducing intervals. All action types were given a larger range of times to select, but instead of checking movements at every moment of time, we used the step property in range to lower the granularity of how close the times checked were together.
Giving a different time range to the s action. As s is generally used to wait for an asteroid to go by, we gave it a less granular checking interval (every ten as opposed to every five), but increased the amount of time the ship could wait for, so it could wait a bit longer for asteroids moving at different speeds to reach a preferable alignment.

Data:
-   Look at the image in this Github Repo that will show the comparison of times from the original code and the modified code.
-   The file is called: DataTime.png

How It Works:
-   The way the tree search works is by using a BFS search algorithm which will use nodes as the way to keep track of the paths. A stack is used to hold the nodes of the tree, the stack is popped when the .next() function is called and that will contain the next node to go to. The loop will check if the current node is the SUCCESS node which means that the ship has made it to the other side of the board. If the current node is not at the other side of the board then that means that it will try and explore more paths which means it will call expand() which means it will look at the possible paths that it can take, such as e, d, c, and s. 


Any problems that occured:
-   There were not many problems that occured. 
    The team had to deal with Windows/Unix compatability at the start and that was a bit annoying to deal with. After that was sorted out the team was able to better work together. Realizing that some libraries needed to be commented out. 
    I was using a Mac to run the simulations and sometimes I used had stalling problems when I tried to the run the simulations. Certain game JSONs would not finish. 
    