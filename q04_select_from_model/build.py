# Default imports
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

data = pd.read_csv('data/house_prices_multivariate.csv')


# Your solution code here
def select_from_model (df):
    X, y = df.iloc[:,:-1], df.iloc[:,-1]
    selected = SelectFromModel(RandomForestClassifier(random_state=9))
    selected.fit(X,y)
    return  X.columns.values[selected.get_support()].tolist()

print select_from_model(data)
