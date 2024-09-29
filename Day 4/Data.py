import pandas as pd 
import seaborn as sns
link = pd.read_csv('D:\Data Science ML\Day 4\linkedin-reviews.csv')
print(link)

# 1. scatterplot(Numerical column - Numerical column)

sns.scatterplot(x=link['total_bill'],   #df['total_bill']
                y= link['tip'])


