## Authors: Brian Rauh and Isaias Villabos
Results indicate that our Tree Search is generally the fastest algorithm, though its fuel usage begins to eclipse the others in the later—generally larger—games. The simulated annealing and genetic algorithms both tended to be more consistent in fuel usage, however, as a result of the methods we used to generate them encouraging them to be longer rather than shorter, as we had some problems with getting stuck in states where a short, unfinished path appeared to the algorithm to be preferable to a longer path with collisions (which could then later be fixed to be a correct answer).
<br>Unfortunately, the generation of our steps data was incorrect, and as a result not much can be taken away from the chart or table themselves, but I suspect, were they properly formed, that they would find both the simulated annealing and genetic algorithms were much more regularly a perfect (or near-perfect) fit to the board length, as, once again, the generation of their moves occurred with the window width in mind, while the tree search moves were created by trying a variety of lengths within a wide range, which leaves a lot of room for potentially overshooting the far boundary.

# Instructions for viewing data:
All of our charts and tables are generated through the charts.py file, and a sample of the output with one run on bar charts is included in the "Charts and Tables" folder in this repository. Regretably, the step data is corrupted.

# Algorithm Pseudocode below
    Simulated Annealing Pseudocode
        Agent creation
        Temperature initalized to 0
        Inital path created
        While True
            Temperature increases, and is fed into the scheduler to get T, calculated with 1/temp
            Loop breaks if T is 0, which it is set to at iteration 1000
            A successor to the current path is created by adding, deleting, or swapping a move
            The difference in value between the successor and the current path is found, and the successor is accepted if it is higher
            Otherwise, the successor is chosen with a probability based on the difference in value and current T value
    
    Genetic Algorithm Pseudocode
        while infinite:

        population_list = call createPopulation() 
                                --> calls createPopulation() which calls fitnessFunction()
                                --> calls generatePopulation() 
                                --> calls fitnessFunction()
        call mutatePopulation on population_list
                                --> calls mutatePopulation()
        if there are fit inviduals
            return the list of fit inviduals
            
    Pseudocode for functions used in Genetic Algorithm 
        createPopulation():
            for i = 1 in range(populationSize):
                call generatePopulation()
                
        mutatePopulation():
            call RandomSlection() to introduce variability
            
        fitnessFunction():
            check if distance traveled by an indivodual equals screen_width
            remove indivudals that do not meet above criteria
            return list
            
        generatePopulation():
            create list
            create random distance value
            create random direction vale
            
        randomSelection():
            choose random distance value based on screen width 
            choose random direction based on [e,s,d,c]
        
    Tree Search Psuedocode for the changes made by Team Brian and Isaias
    
    for every move in the set [e,d,c,s]
        if the parent first move is in the set and a parent node exists
            skip
        if the action is "s":
            if the ship has 1 fuel:
                skip
            else:
                for time = 0 to 201 seconds
                    call act() given a state, action, and time
                    call Node() on the state action and time
                    assign child to the leaves array
        else:
            for time = 0 until 101
                call act() on the state, action and time
                call Node() on the state, action and time
                assign the child to the leaves array
        return the values of the leaves dictionary

##Good work. Not performed multiple times and box and whisker plot missing -10