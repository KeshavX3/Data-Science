# -*- coding: utf-8 -*-
"""Day5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gT72lKr6kiYt6qC2lKiyiKpYrmzUMnAd
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/covid_toy.csv')

df

df.head(2)

df = df.dropna()

df.head(2)

df = df.drop(columns=['age' , 'fever'])

df.head(2)

df

"""# Ordinal Encodering"""

from sklearn.preprocessing import OrdinalEncoder

oe = OrdinalEncoder(categories = [['Male' , 'Female'] , ['Mild' , 'Strong'] , ['Kolkata' , 'Bangalore' , 'Delhi' , 'Mumbai'] , ['No' , 'Yes']])

df_new = oe.fit_transform(df)

df_new_2 = pd.DataFrame(df_new , columns = df.columns)

df_new_2

"""# **OneHot Encoder**"""

df = pd.read_csv('/content/covid_toy.csv')

df = df.dropna()

from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder(sparse = False , drop = 'first' , dtype = np.int32)

df_new = ohe.fit_transform(df[['gender' , 'cough' , 'city' , 'has_covid']])

df.head(2)

df_new.shape

df_new

"""# **Coulmn Transformer**"""

import numpy as np
import pandas as pd

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder

df = pd.read_csv('/content/covid_toy.csv')

df

df.isnull().sum()

from  sklearn.model_selection import train_test_split

x_train , x_test , y_train , y_test = train_test_split(df.drop(columns = ['has_covid']) , df['has_covid'] , test_size = 0.2 , random_state = 42)

x_train

"""## **Manually type output**"""

# adding simple imputer to fever column
si = SimpleImputer()
x_train_fever = si.fit_transform(x_train[['fever']])

# also the test data
x_test_fever = si.transform(x_test[['fever']])

x_train_fever.shape

# Ordinal Enconding  ----> cough

oe = OrdinalEncoder(categories = [['Mild' , 'Strong']])
x_train_cough = oe.fit_transform(x_train[['cough']])

# also the test data
x_test_cough = oe.transform(x_test[['cough']])

x_train_cough.shape

# OneHot Encoding ---> gender , city
ohe = OneHotEncoder(drop = 'first', sparse = False )
x_train_gender_city = ohe.fit_transform(x_train[['gender' , 'city']])

# also the test data
x_test_gender_city = ohe.transform(x_test[['gender' , 'city']])

x_train_gender_city.shape

# Extacting Age

x_train_age = x_train.drop(columns = ['fever' , 'cough' , 'gender' , 'city']).values

#aslo the test data
x_test_age = x_test.drop(columns = ['fever' , 'cough' , 'gender' , 'city']).values

x_train_age.shape

x_train_transformed  = np.concatenate((x_train_fever , x_train_cough , x_train_gender_city , x_train_age) , axis = 1)

x_train_transformed.shape

"""# **BY the help of Column transformer**"""

from sklearn.compose import ColumnTransformer   # this os how to import column trnsfomer

transformer = ColumnTransformer(transformers=[
    ('tnf1' , SimpleImputer() , ['fever']),
#    filll missing values by mean , medain , mode .
    ('tnf2' , OrdinalEncoder(categories = [['Mild' , 'Strong']]) , ['cough']),
#    we encode out data
    ('tnf3' , OneHotEncoder(drop = 'first', sparse = False) , ['gender' , 'city']),
    ] , remainder = 'passthrough')    #remainder  = pass through it means rest all the pass

transformer.fit_transform(x_train).shape

"""# **Pipeline on covid data **"""

import numpy as np
import pandas as pd

df = pd.read_csv('/content/covid_toy.csv')
df.head()

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler , OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

x_train , x_test , y_train , y_test = train_test_split(
    df.drop('has_covid' ,  axis = 1) , df['has_covid'] , test_size = 0.2 ,
    random_state = 42)

#Define the columns thaht need to be prerocessed
categorical_features = ['gender' , 'city']
numeric_features = ['fever' , 'age' ]

#create Transformers
numeric_transformer = Pipeline(steps=[
    ('imputer' , SimpleImputer(strategy = 'mean')),
    ('scaler' , StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer' , SimpleImputer(strategy = 'most_frequent')),
    ('onehot' , OneHotEncoder(handle_unknown = 'ignore'))
])

#combine Tnasdformers
preprocessor = ColumnTransformer(
    transformers=[
        ('num' , numeric_transformer , numeric_features),
        ('cat' , categorical_transformer , categorical_features)
    ])

#create pipeline
clf = Pipeline(steps=[
    ('preprocessor' , preprocessor),
    ('classifier' , LogisticRegression())])

#Train  the model
clf.fit(x_train , y_train)

#Evaluate the model
y_pred = clf.predict(x_test)

y_pred

from sklearn.metrics import accuracy_score
accuracy_score(y_test , y_pred)

"""# Pipeline for Network ads data"""

import numpy as np
import pandas as pd

df = pd.read_csv('/content/Social_Network_Ads.csv')

df.head()

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler , OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

x_train , x_test , y_train , y_test = train_test_split(
    df.drop('Purchased' ,  axis = 1) , df['Purchased'] , test_size = 0.2 ,
    random_state = 42)

categorical_features = ['Gender']
numeric_features = ['User ID' , 'Age' , 'EstimatedSalary']

#create Transformers
numeric_transformer = Pipeline(steps=[
    ('imputer' , SimpleImputer(strategy = 'mean')),
    ('scaler' , StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer' , SimpleImputer(strategy = 'most_frequent')),
    ('onehot' , OneHotEncoder(handle_unknown = 'ignore'))
])

#combine Tnasdformers
preprocessor = ColumnTransformer(
    transformers=[
        ('num' , numeric_transformer , numeric_features),
        ('cat' , categorical_transformer , categorical_features)
    ])

#create pipeline
clf = Pipeline(steps=[
    ('preprocessor' , preprocessor),
    ('classifier' , LogisticRegression())])

#Train  the model
clf.fit(x_train , y_train)

#Evaluate the model
y_pred = clf.predict(x_test)

y_pred

from sklearn.metrics import accuracy_score
accuracy_score(y_test , y_pred)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""# **Piple for Tips data **"""

df = pd.read_csv('/content/tips.csv')

df.head()

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler , OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

x_train , x_test , y_train , y_test = train_test_split(
    df.drop('total_bill' ,  axis = 1) , df['total_bill'] , test_size = 0.2 ,
    random_state = 42)

categorical_features = ['sex' , 'smoker' , 'day' , 'time']
numeric_features = ['tip' , 'size']

#create Transformers
numeric_transformer = Pipeline(steps=[
    ('imputer' , SimpleImputer(strategy = 'mean')),
    ('scaler' , StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer' , SimpleImputer(strategy = 'most_frequent')),
    ('onehot' , OneHotEncoder(handle_unknown = 'ignore'))
])

#combine Tnasdformers
preprocessor = ColumnTransformer(
    transformers=[
        ('num' , numeric_transformer , numeric_features),
        ('cat' , categorical_transformer , categorical_features)
    ])

#create pipeline
clf = Pipeline(steps=[
    ('preprocessor' , preprocessor),
    ('classifier' , LinearRegression())])

#Train  the model
clf.fit(x_train , y_train)

#Evaluate the model
y_pred = clf.predict(x_test)

y_pred

from sklearn.metrics import r2_score
r2 = r2_score(y_test , y_pred)

r2

"""# Social Network with missing data"""

import numpy as np
import pandas as pd

df = pd.read_csv('/content/Social_Network_Ads.csv')

df

print(x_train.shape)

from  sklearn.model_selection import train_test_split


x_train, x_test, y_train, y_test = train_test_split(df.drop(columns=['Gender']), df['Gender'], test_size=0.2, random_state=42)

# Drop 5 values
x_train.drop(x_train.index[:5], inplace=True)

print(x_train.shape)

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer

# Load the CSV file


# Drop 5 values from the Gender column
idx_to_drop_gender = np.random.choice(df[df['Gender'].notna()].index, size=5, replace=False)
df.drop(idx_to_drop_gender, inplace=True)

# Drop 10 values from the Estimated Salary column
idx_to_drop_salary = np.random.choice(df[df['EstimatedSalary'].notna()].index, size=10, replace=False)
df.drop(idx_to_drop_salary, inplace=True)

# Label encode the Gender column
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])

# Impute missing values in the Estimated Salary column
imputer = SimpleImputer(strategy='mean')
df[['EstimatedSalary']] = imputer.fit_transform(df[['EstimatedSalary']])

# Print the resulting DataFrame
print(df.head())

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

# Load the CSV file


# Drop 5 values from the Gender column
idx_to_drop_gender = np.random.choice(df[df['Gender'].notna()].index, size=5, replace=False)
df.drop(idx_to_drop_gender, inplace=True)

# Drop 10 values from the Estimated Salary column
idx_to_drop_salary = np.random.choice(df[df['EstimatedSalary'].notna()].index, size=10, replace=False)
df.drop(idx_to_drop_salary, inplace=True)

# Define the preprocessing steps for each column
categorical_cols = ['Gender']
numerical_cols = ['EstimatedSalary']

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')), # Use 'missing' for categorical
    ('encoder', LabelEncoder())
])

numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')), # Use 'mean' for numerical
    ('scaler', StandardScaler())
])

preprocessor = ColumnTransformer(
    transformers=[
        ('categorical', categorical_transformer, categorical_cols),
        ('numerical', numerical_transformer, numerical_cols)
    ]
)

# Create a pipeline with the preprocessor and fit it to the data
pipeline = Pipeline(steps=[('preprocessor', preprocessor)])
pipeline.fit(df)

# Transform the data using the pipeline
df_transformed = pipeline.transform(df)

# Convert the transformed data back to a DataFrame
df_transformed = pd.DataFrame(df_transformed, columns=df.columns)

# Print the resulting DataFrame
print(df_transformed.head())

# Name =  Saurabh Soni
# Email =  Saurabhsonibrd@gmail.com , contact@regexsoftware.com
# Mob NO - 7300167130
# HR Manager - Prachi
# Address =  Near Cake world , Gopalpura Bye Pass (Regex Software Pvt. Ltd)

