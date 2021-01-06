import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import tree
from sklearn import datasets, linear_model
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import precision_recall_fscore_support

# download Titanic dataset and place in your working directory, so that this command will find your file
train = pd.read_csv("train.csv")
# test = pd.read_csv("test.csv")
#
# # Divide input data X from labeled values to predict Y
x_train = train.loc[:, 'Pclass':]
y_train = train.loc[:, 'Survived']

print(x_train)
print(y_train)

#
# # Divide input data X from labeled values to predict Y
# x_test = test.loc[:, 'Pclass':]
# y_test = test.loc[:, 'Age']
#
# print(x_train, x_test)
# print(y_train, y_test)


# split into test and train
# X_train = x_train[:len(x_train)/2]
# X_test = x_train[-len(x_train)/2:]


# Clean up the data a bit so that it can processed by the decision tree
# A more serious attempt would extract more subtle features from the data.
x_train['Embarked'] = [0 if str(name) == "nan" else ord(name) for name in x_train['Embarked']]
x_train['Cabin'] = [0 if str(el) == "nan" else len(str(el)) for el in x_train['Cabin']]
x_train['Ticket'] = [0 if str(el) == "nan" else len(str(el)) for el in x_train['Ticket']]

def sumASCII(name):
    accum = 0
    for i in name:
        accum += ord(i)
    return accum

x_train['Name'] = [0 if str(name) == "nan" else sumASCII(str(name)) for name in x_train['Name']]
x_train['Sex'] = [0 if sex == 'male' else 1 for sex in x_train['Sex']]


# Just give up on these for now
# X = X.drop(['Ticket', 'Cabin', 'Embarked'], axis = 1)
x_train = x_train.fillna(0)

clf = MLPClassifier(solver='lbfgs',alpha=1e-5,hidden_layer_sizes=(5,2),random_state=1)
clf.fit(x_train,y_train)

y_pred = clf.predict(x_train)

y_true = y_train

print(precision_recall_fscore_support(y_true, y_pred, average='macro'))


# Plot outputs

fig = plt.figure(figsize=(100,100))

# plt.plot(x_train, y_pred, color='blue', linewidth=10)
#
# plt.xticks(())
# plt.yticks(())
#
# plt.show()

