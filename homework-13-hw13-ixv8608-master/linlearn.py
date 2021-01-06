import numpy as np
import pandas as pd
from scipy import stats, optimize

## Read data (20 points)
def readData():
    df = pd.read_csv("week13_data.csv")
    return df

## Determine value of the 40 linear parameters w0, ...,
# w39, by discovering the values that minimize the
# mean squared error between the true values (yi)
# and the predicted values w0xi0 + ... + w39xi39.
# You may use analysis or gradient descent (i.e., hill climbing,
# or descending in this case) (60 points)
def solve(dataframe, y):
    # This dataframe contains all the data for the X Columns
    X_Columns = dataframe.drop(columns=['y'])

    # This will transpose the matrix, X_Columns
    X_Transpose = np.transpose(X_Columns)

    # This will find the product of X Transpose multiplied with X_Columns
    X_Products = np.matmul(np.array(X_Transpose), np.array(X_Columns))

    # Find the inverse
    X_Inverse = np.linalg.inv(np.array(X_Products))

    # Take inverse and multiply it with transpose
    X_InverseTransposeProduct = np.matmul(np.array(X_Inverse), np.array(X_Transpose))

    # Calculate, inverse X transpose X y, to get w
    w_i = np.matmul(np.array(X_InverseTransposeProduct), np.array(y))

    # Format the dataframe, the first entry is just a blank for the ColumnName row, and the
    # column value row
    df = pd.DataFrame(data=list(w_i), index=[X_Columns.columns.values], columns=[" "])

    # Output to CSV with proper name, params.csv
    df.transpose().to_csv("params.csv")

# Small little helper functions
def computePredicted(dataframe):
    expectedValues = dataframe['y']
    solve(dataframe, expectedValues)

## Output answers as params.csv. T
# his should have two rows: one for the labels
# w0, ..., w39 and one for the values (20 points)

if __name__ == '__main__':
    dataframe = readData()
    computePredicted(dataframe)