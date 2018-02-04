# Default imports
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier


# Your solution code here
def rf_rfe(df):
    X, y = df.iloc[:,:-1], df.iloc[:,-1]
    model =RandomForestClassifier()
    # create the RFE model and select 3 attributes
    rfe = RFE(model)
    rfe = rfe.fit(X, y)
    #print rfe.ranking_
    return X.columns.values[rfe.get_support()].tolist()

#print (rf_rfe(data))
