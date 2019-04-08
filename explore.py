import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_train = pd.read_csv('train.csv')
df_test = pd.read_csv('test.csv')

# print('Explore Training Data')
# print(df_train.columns)
# print(df_train.dtypes)
# print(df_train.shape)
# print(df_train.head())

# print(df_train['Loan_Status'].value_counts())
# print(df_train['Loan_Status'].value_counts(normalize = True))
# df_train["Loan_Status"].value_counts().plot.bar()

print(df_train.isnull().sum())

# print('\n\nExplore Testing Data')
# print(df_test.columns)
# print(df_test.dtypes)
# print(df_test.shape)
# print(df_test.head())