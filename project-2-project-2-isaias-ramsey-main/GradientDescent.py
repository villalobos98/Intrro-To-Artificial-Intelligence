import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import tree
from sklearn import datasets, linear_model
from sklearn.linear_model import SGDClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import precision_recall_fscore_support
from sklearn.linear_model import SGDClassifier
from sklearn.datasets import make_blobs

# download Titanic dataset and place in your working directory, so that this command will find your file
train = pd.read_csv("train.csv")
#
# Divide input data X from labeled values to predict Y
x_train = train.loc[:, 'Pclass':]
y_train = train.loc[:, 'Survived']

# Used to check and see what is inside the dataset
# print(x_train)
# print(y_train)


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

# Cleaning the data for feature, Name and Sex
x_train['Name'] = [0 if str(name) == "nan" else sumASCII(str(name)) for name in x_train['Name']]
x_train['Sex'] = [0 if sex == 'male' else 1 for sex in x_train['Sex']]


# Just give up on these for now
x_train = x_train.fillna(0)


clf = SGDClassifier(loss="hinge",alpha=0.01,max_iter=200)
clf.fit(x_train,y_train)

# This predict function is a way to give labels for samples in x_train.
y_pred = clf.predict(x_train)
y_true = y_train

# The precision_recall_fscore_support function will compute the
# precision, recall, F-measure and support for each class

precision, recall, fscore, support = precision_recall_fscore_support(y_true, y_pred, average='macro')
print("Precision value is", precision)
print("Recall value is", recall)
print("Fscore value is", fscore)

# # Plot outputs
# xx = np.linspace(-1, 5, 10)
# yy = np.linspace(-1, 5, 10)

# X1, X2 = np.meshgrid(xx, yy)
# Z = np.empty(X1.shape)
# for (i, j), val in np.ndenumerate(X1):
#     x1 = val
#     x2 = X2[i, j]
#     p = clf.decision_function([[x1, x2]])
#     Z[i, j] = p[0]
# levels = [-1.0, 0.0, 1.0]
# linestyles = ['dashed', 'solid', 'dashed']
# colors = 'k'
# plt.contour(X1, X2, Z, levels, colors=colors, linestyles=linestyles)
# plt.scatter(x_train[:, 0], x_train[:, 1], c=Y, cmap=plt.cm.Paired,
#             edgecolor='black', s=20)

# plt.axis('tight')
# plt.show()


# fig = plt.figure(figsize=(100,100))
#
#
# plt.plot(x_train, y_pred, color='blue', linewidth=5)
#
# plt.xticks(())
# plt.yticks(())
#
# plt.show()
