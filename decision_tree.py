# -------------------------------------------------------------------------
# AUTHOR: Shane Dirksen
# FILENAME: decision_tree.py
# SPECIFICATION: A simple python program that takes a specific csv input, changes the feature values to integers, and generates a decision tree.
# FOR: CS 4210- Assignment #1
# TIME SPENT: 3 hours
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to
# work here only with standard dictionaries, lists, and arrays

# importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv

db = []
X = []
Y = []

# reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row)
            print(row)

# transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1,
# Prepresbyopic = 2, Presbyopic = 3 so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]] --> add your Python code here

for entry in db:
    updated_instance = []
    for i, value in enumerate(entry):
        if i == 0:
            if value == 'Young':
                updated_instance.append(1)
            elif value == 'Prepresbyopic':
                updated_instance.append(2)
            elif value == 'Presbyopic':
                updated_instance.append(3)
        elif i == 1:
            if value == 'Myope':
                updated_instance.append(1)
            elif value == 'Hypermetrope':
                updated_instance.append(2)
        elif i == 2:
            if value == 'No':
                updated_instance.append(1)
            elif value == 'Yes':
                updated_instance.append(2)
        elif i == 3:
            if value == 'Reduced':
                updated_instance.append(1)
            elif value == 'Normal':
                updated_instance.append(2)
    X.append(updated_instance)

# transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1,
# No = 2, so Y = [1, 1, 2, 2, ...] --> addd your Python code here
for entry in db:
    if entry[-1] == 'Yes':
        Y.append(1)
    elif entry[-1] == 'No':
        Y.append(2)

# fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion='entropy', )
clf = clf.fit(X, Y)
# plotting the decision tree

tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes', 'No'], filled=True,
               rounded=True)
plt.show()
