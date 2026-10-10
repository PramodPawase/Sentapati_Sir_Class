import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#get  the datset

data_set=pd.read_csv(r'C:\Users\Pramod\OneDrive\AI Python\Senapati Sir\Class Document\ML_All_Class\7OCT_ML\Data.csv')

#print the the dataset
print(data_set)
print('=============================')
#Filter the data base on the x,y

x=data_set.iloc[:,-1].values
y=data_set.iloc[:,-1].values

print(f'the value if x is {x} ')
print('\n')

print(f'the value of y is {y}')
print('=========================')

print('====import the module to apply mean strategy for null values=====')

from sklearn.impute import SimpleImputer # SPYDER 4 
imputer = SimpleImputer(strategy="mean")  #create object for simpleimputer class

print("=====apply the filter====")
imputer.fit(x[:,1:3]) 

x[:, 1:3] = imputer.transform(x[:,0:2])


