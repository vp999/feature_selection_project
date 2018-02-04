# Default imports

import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import f_regression


# Write your solution here:

def percentile_k_features (df, k=20):
    predictors = df.drop(['SalePrice'], axis=1)
    target_variable= df['SalePrice']
    selector= SelectPercentile(f_regression, percentile=k)
    selector.fit_transform(predictors, target_variable)

    names = predictors.columns.values[selector.get_support()]
    scores = selector.scores_[selector.get_support()]
    names_scores = list(zip(names, scores))
    ns_df = pd.DataFrame(data = names_scores, columns=['Feat_names', 'F_Scores'])
    #Sort the dataframe for better visualization
    ns_df_sorted = ns_df.sort_values(['F_Scores', 'Feat_names'], ascending = [False, True])
    return ns_df_sorted['Feat_names'].tolist()


print percentile_k_features(data)
