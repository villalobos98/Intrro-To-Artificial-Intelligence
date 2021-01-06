Isaias Villalobos and Brian Rauh

Explanation of Cleaning the data:
The data for the Embarked, Ticket, and Cabin needed to be changed
into values that could be processed correctly by the fit() function.
The simplest change was to the name to its ASCII value if it existed and
0 if it did not exist.
<br>The same idea applied to the other features, Ticket, and Cabin, which also needed
to have the same logic applied. The best way to handle that was with list comprehension.
The "Name" feature needed to be changed into a value so the way that handled was by find the ASCII
value of each of the characters in the string and adding them to an accumulator. 
Handling the NaN was the most interesting part, but the way that is handled is by simply updating the NaN
to be a 0 value. 

The value of the precision_f_score_recall is (1.0, 1.0, 1.0, None)


