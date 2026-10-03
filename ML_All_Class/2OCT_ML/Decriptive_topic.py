import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt




incom_df=pd.read_csv(r'C:/Users/Pramod/OneDrive/AI Python/Senapati Sir/Class Document/ML_All_Class/2OCT_ML/Inc_Exp_Data.csv')

#print(incom_df)
print('\n')

tt=incom_df.describe().T  #transforse the
#print(tt)

#to check is any missing values
is_mis_values=incom_df.isna().any()
print(is_mis_values)

#apply column values - central tendancy - 

col1=incom_df['Mthly_HH_Expense'].mean()
print(col1)

col2=incom_df['Mthly_HH_Expense'].median()
print(col2)

col3=incom_df['Mthly_HH_Expense'].mode()
print(col3)

print('\n')
print('\n')

print('=============================')

max_exp_temp=pd.crosstab(index=incom_df['Mthly_HH_Expense'],columns="count")

max_exp_temp.reset_index(inplace=True)

#incomplited 
#max_exp_temp[max_exp_temp["count"]=incom_df.Mthly_HH_Expense.value_counts.count()]


print('=======find quantile - quator profit=====')

qut_prof=incom_df['Mthly_HH_Expense'].quantile(0.75)
print(qut_prof)

qut_prof1=incom_df['Mthly_HH_Expense'].quantile(0.25)
print(qut_prof1)

IQR=incom_df['Mthly_HH_Expense'].quantile(0.75)-incom_df['Mthly_HH_Expense'].quantile(0.25)
print(IQR)


print('================Variance=============')
variance = incom_df['Mthly_HH_Expense'].var()
print(variance)

print('================Standard Deviation=============')
std_dev = incom_df['Mthly_HH_Expense'].std()
print(std_dev)