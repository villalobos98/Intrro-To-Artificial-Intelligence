from sklearn import tree, metrics
import pandas as pd
import matplotlib.pyplot as plt

train=pd.read_csv("train.csv") # download Titanic dataset and place in your working directory, so that this command will find your file
clf = tree.DecisionTreeClassifier()

# Divide input data X from labeled values to predict Y
X = train.loc[:,'Pclass':]
Y = train.loc[:,'Survived']

# Clean up the data a bit so that it can processed by the decision tree
# A more serious attempt would extract more subtle features from the data.
X['Embarked'] = [0 if str(name) == "nan" else ord(name) for name in X['Embarked']]
X['Cabin'] = [0 if str(el) == "nan" else len(str(el)) for el in X['Cabin']]
X['Ticket'] = [ 0 if str(el) == "nan" else len(str(el)) for el in X['Ticket']]

def sumASCII(name):
    accum = 0
    for i in name:
        accum += ord(i)
    return accum

X['Name'] = [0 if str(name) == "nan" else sumASCII(str(name)) for name in X['Name']]
X['Sex'] = [0 if sex == 'male' else 1 for sex in X['Sex']]

# Just give up on these for now
# X = X.drop(['Ticket', 'Cabin', 'Embarked'], axis = 1)
X = X.fillna(0)

# train the model
clf = clf.fit(X, Y)

# run predictions on the data, using the model. They should mostly conform to the training values Y
y_pred = clf.predict(X)
fig = plt.figure()
_ = tree.plot_tree(clf, feature_names=X.columns, filled=True)
returnVal = metrics.precision_recall_fscore_support(Y, y_pred, average="macro")
print(returnVal)


fig.savefig("tree.png")
plt.show()
