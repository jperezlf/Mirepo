import pandas
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle
import sys

np.set_printoptions(threshold=sys.maxsize)
pandas.set_option('display.max_rows', 500)
pandas.set_option('display.max_columns', 500)
pandas.set_option('display.width', 1000)

def mean_absolute_error(y_true, y_pred):
    """Calculates MAE given y_true and y_pred"""
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs(y_true - y_pred))


# load data
if sys.argv[1]:
    path_to_project = sys.argv[1]
    data = pandas.read_csv(path_to_project + '/crones_datos/file.csv', header=0)
else:
    data = pandas.read_csv('training.csv', header=0)
dataset = data.drop_duplicates()
feature_names = dataset.columns.values

features_to_delete = np.array(['Temperature'])
feature_names = np.setdiff1d(feature_names, features_to_delete)

Y_train = dataset.filter(items=['Temperature']).astype('int64')
X_train = dataset.filter(items=feature_names).astype('int64')

tree = DecisionTreeClassifier(random_state=0)
tree.fit(X_train, Y_train)

if sys.argv[1]:
    name = path_to_project + '/algorithms/DecisionTreeClassifier/model/train.dat'
else:
    name = 'train.dat'
pickle.dump(tree, open(name, "wb"))