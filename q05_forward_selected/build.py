# Default imports
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv('data/house_prices_multivariate.csv')

model = LinearRegression()


# Your solution code here
from  sklearn.metrics import r2_score
from operator import itemgetter
import numpy as np

def get_r2score_for_feature(X,y,featurename):
    model.fit(X,y)
    return list((featurename, r2_score(y, model.predict(X))))

def get_featurelist_for_iteration(selected_features,columnname):
    # created to get new list with additonal value.Note: Append does in place add.
    iteration_features =selected_features[:]
    iteration_features.append (columnname)
    return iteration_features

def forward_selected (data, model):
    features, target_variable = data.iloc[:,:-1], data.iloc[:,-1]
    selected_features =list()
    selected_r2_scores= list()

    #start with zero feature and keep adding one in each iteration
    for i in range (1,len(features.columns) ):
        # Add each feature one at a time and check the r2square and get best one
        scores_iterations = [ get_r2score_for_feature(
                                                    features.loc[:
                                                        , get_featurelist_for_iteration (
                                                            selected_features,colname)]
                                                    ,target_variable, colname)
                            for colname in features]

        scores_iterations = sorted(scores_iterations, key=itemgetter(1),reverse=True)

        # add details of best_feature selected in iteration to carry forward next iteration
        selected_features.append( scores_iterations[0][0])
        selected_r2_scores.append( scores_iterations[0][1])

    return selected_features, selected_r2_scores


#print forward_selected(data, model)
