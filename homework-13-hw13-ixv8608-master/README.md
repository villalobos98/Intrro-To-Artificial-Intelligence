    @author: Isaias Villalobos
    @date: 11/16/2020
    @HW#: 13
    @Description: The code that I wrote in linlearn.py is supposed to model a linear
                    regression.
                    In order to do this, I had to first, determine the value of the 40 linear parameters
                    which are for example, w0, w1, w2, etc by discovering the values that minimize the
                    mean squared error between the true values (yi)
                    and the predicted values w0xi0 + ... + w39xi39.
                    
                    The readData() functions simply takes the data and reads the data into a dataframe.
                    The values that were given, were X columns with their associated X values. 
                    The dataframe also contained the expected values, y, to be used when calculating W
                    The equation, W = ((X^T*X)^-1)(X^t)(y), was implemented in the solve function
                    to get the 40 wight values, w, that were needed.
                    
                        