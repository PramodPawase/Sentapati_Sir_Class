import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt #visualizations
import seaborn as sns
import warnings

emp = pd.read_excel(r"C:/Users/Pramod/OneDrive/AI Python/Senapati Sir/Class Document/30th_sep_class/Rawdata.xlsx")
# get info
print(emp.info())

#get toltal column
columns=emp.columns
print(columns)

#print the shape of the data
shape=emp.shape
print(shape)

#print the index of the data
index=emp.index 
print(index)

#print the tail of the data
tail=emp.tail()
print(tail)

#print the Domain columns
domain_columns=emp['Domain']
print(domain_columns)

#print isnull values
isnull_values=emp.isnull().sum()
print(isnull_values)

# print the name column values
name_column=emp['Name']
print(name_column)

#clean the name column values
print('==================Clean the Name Column=====================')

emp['Name'] = emp['Name'].str.replace(r'\W','',regex=True)
print(emp['Name'])

print('=============print the head 1 rows of the data=====================')
print(emp.head(1))

print('=============clean the Domain Column=====================')
emp['Domain'] = emp['Domain'].str.replace(r'\W','',regex=True)
print(emp['Domain'])

print('=============print the all of the data=====================')
emp_List=emp
print(emp_List) 

print('=============clean the Location column values=====================')
emp['Location'] = emp['Location'].str.replace(r'\W','',regex=True)
print(emp['Location'])

print('=============Clean the Age Column=====================')

emp['Age']=emp['Age'].str.replace(r'\W','',regex=True)
print(emp['Age'])

print('=============Age column get only digit=====================')
emp['Age']=emp['Age'].str.extract('(\\d+)') # r(r'(\\d+)')
print(emp['Age'])

print('=============Clean the Salary Column=====================')
emp['Salary']=emp['Salary'].str.replace(r'\W','',regex=True)
print(emp['Salary'])


print('=============Experience column get only digit=====================')
emp['Exp']=emp['Exp'].str.extract('(\\d+)')
print(emp['Exp'])

print('`````````````````````````````````````````````````')

print('\n')

print('\n')

print('=============Creat clean array copy of the data=====================')

Clean_array=emp.copy()
print(Clean_array)


print('=============#### till now we have raw data we use regex to clean the data and removed all noise characted from the dataset====')
print('#### you can also work in same things in sql query as well=====================')

print('\n')

print('\n')
print('=============Age Column missing values treatment for numerical data =====================')

print(Clean_array)
Clean_array['Age']=Clean_array['Age'].fillna(np.mean(pd.to_numeric(Clean_array['Age'])))
print(Clean_array['Age'])

print('=============Exp Column missing values treatment for categorical data =====================')

Clean_array['Exp']=Clean_array['Exp'].fillna(np.mean(pd.to_numeric(Clean_array['Exp'])))
print(Clean_array['Exp'])


print('====Location get sum of all null values====')

loc_nan=Clean_array['Location'].isnull().sum()
print(loc_nan)

print('====Location Column missing values treatment for categorical data =====================')
Clean_array['Location']=Clean_array['Location'].fillna(Clean_array['Location'].mode()[0])
print(Clean_array['Location'])

print('====print the info====')
print(Clean_array.info())

print('====Convert object column to integer====')
Clean_array['Age']=Clean_array['Age'].astype(int)
Clean_array['Salary']=Clean_array['Salary'].astype(int)
Clean_array['Exp']=Clean_array['Exp'].astype(int)

print(Clean_array.info())


print('====convert the column in to the categorical data type====')
Clean_array['Domain']=Clean_array['Domain'].astype('category')
Clean_array['Name']=Clean_array['Name'].astype('category')
Clean_array['Location']=Clean_array['Location'].astype('category')

print(Clean_array.info())
print('\n')

print('=============Clean data convert into csv file=====================')
#Clean_array.to_csv(r"C:/Users/Pramod/OneDrive/AI Python/Senapati Sir/Class Document/30th_sep_class/Clean_data_Pramod.csv",index=False)

print('\n')
print('====# EDA TECHNIQUE LETS APPLY======')
warnings.filterwarnings('ignore')
print(Clean_array['Salary'])

