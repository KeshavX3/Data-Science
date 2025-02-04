# -*- coding: utf-8 -*-
"""project gaming

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pQMkfLyCfrUajgecPLBEaV98O9ybKxJl
"""

import numpy as np
import pandas as pd

data=pd.read_csv("/content/online_gaming_behavior_dataset.csv")
print(data.head())

# Handle missing values
data = data.dropna()  # or use imputation methods

# Handle duplicates
data = data.drop_duplicates()

"""# ***Player Segmentation Analysis***

## Introduction

This document outlines the analysis performed on player engagement data focusing on the demographic factor: age. The goal is to understand how player age impacts engagement levels in online gaming.

## Data Overview

The dataset contains information on various player attributes, including age and engagement level. For this analysis, the primary columns of interest are:
"""

import matplotlib.pyplot as plt
import seaborn as sns

# Check column names and correct if necessary
print(data.columns)  # Print columns to verify the exact name

plt.figure(figsize=(10, 6))
# Adjust column name below if needed based on the output above
sns.histplot(data['Age'], bins=30, kde=True)  # Changed 'age' to 'Age'
plt.title('Distribution of Player Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()



df=pd.read_csv("/content/online_gaming_behavior_dataset.csv")
df

df.head(2)

df=df.dropna()
df

from sklearn.preprocessing import OneHotEncoder

# ... (rest of your code)

encoder = OneHotEncoder(sparse_output=False)  # Using the recommended 'sparse_output' argument

ohe = OneHotEncoder(drop='first',sparse=False,dtype=np.int32 )

df_new = ohe.fit_transform(df[['Gender','Location','GameGenre','GameDifficulty','EngagementLevel']])

df.head(2)

df_new.shape

df_new

import numpy as np
import pandas as pd

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder

df.isnull().sum()

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(df.drop(columns=['EngagementLevel']),df['EngagementLevel'],test_size=0.2)

x_train

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder

# Define transformers for each column type
numeric_features = ['Age', 'PlayTimeHours', 'SessionsPerWeek', 'AvgSessionDurationMinutes', 'PlayerLevel', 'AchievementsUnlocked']
numeric_transformer = SimpleImputer(strategy='mean')

categorical_features = ['Gender', 'Location', 'GameGenre', 'GameDifficulty'] # Removed 'EngagementLevel' as it's the target variable
categorical_transformer = OneHotEncoder(drop='first', sparse=False)

transformers = [
    ('num', numeric_transformer, numeric_features),
    ('cat', categorical_transformer, categorical_features)
]

# Create ColumnTransformer instance
transformer = ColumnTransformer(transformers=transformers)

transformer.fit_transform(x_train).shape

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

import numpy as np
import pandas as pd

df=pd.read_csv("/content/online_gaming_behavior_dataset.csv")
df

X_train, X_test, y_train, y_test = train_test_split(df.drop('EngagementLevel', axis=1), df['EngagementLevel'], test_size=0.2, random_state=42)

#Define the columns that need to be preprocessed
categorical_features = ['Gender', 'Location', 'GameGenre', 'GameDifficulty' ]
numerical_features = ['PlayerID', 'Age', 'PlayTimeHours', 'SessionsPerWeek', 'AvgSessionDurationMinutes', 'PlayerLevel', 'AchievementsUnlocked'] # Removed tab from 'PlayTimeHours'

# Create transformers

numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])


#Combine Transformers

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features)
    ])


#create the pipeline
clf= Pipeline(steps=[('preprocessor', preprocessor),
                    ('classifier', LogisticRegression())])

#Train the model
clf.fit(X_train, y_train)


#Evaluate the model
y_pred = clf.predict(X_test)

y_pred

from sklearn.metrics import accuracy_score
acc=accuracy_score(y_test, y_pred)
acc

