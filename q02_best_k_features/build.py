# Default imports

import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import f_regression


# Write your solution here:
def percentile_k_features(dataframe, k=20):
    X = dataframe.iloc[:, :-1]
    y = dataframe.iloc[:, -1]
    model = f_regression

    skb = SelectPercentile(model, k)
    predictors = skb.fit_transform(X, y)
    scores = list(skb.scores_)

    top_k_index = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:predictors.shape[1]]
    top_k_predictors = [X.columns[i] for i in top_k_index]

    return top_k_predictors