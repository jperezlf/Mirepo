import pandas
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
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
    data = pandas.read_csv(path_to_project + '/training/training.csv', header=0)
else:
    data = pandas.read_csv('training.csv', header=0)
dataset = data.drop_duplicates()
feature_names = dataset.columns.values

features_to_delete = np.array(['value'])
feature_names = np.setdiff1d(feature_names, features_to_delete)

Y_train = dataset.filter(items=['value'])
X_train = dataset.filter(items=feature_names)

X_train, X_test, Y_train, Y_test = train_test_split(X_train, Y_train, shuffle=True, test_size=0.2, random_state=123)

model = RandomForestRegressor(max_depth=9, n_estimators=1000)

model.fit(X_train, Y_train.values.ravel())

name = path_to_project + '/algorithms/randomforest/model/train.dat'
pickle.dump(model, open(name, "wb"))