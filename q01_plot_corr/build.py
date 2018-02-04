# Default imports
import pandas as pd
from matplotlib.pyplot import yticks, xticks, subplots, set_cmap

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your solution here:
import seaborn as sns
from matplotlib import pyplot as plt
plt.switch_backend('agg')

def plot_corr(df,size=11):
    plt.figure(figsize=(size,6))
    sns.heatmap(df.corr(), cmap='YlOrRd')
    print xticks(), yticks()

#plot_corr(data)
