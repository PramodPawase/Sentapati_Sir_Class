import numpy as np
import matplotlib.pyplot as plt		
import pandas as pd	

dataset = pd.read_csv(r"C:\Users\sayye\Downloads\Salary_Data.csv")
x = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,  y_train)

y_pred = regressor.predict(x_test)

comparison = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(comparison)

plt.scatter(x_test, y_test, color = 'red')
plt.plot(x_train, regressor.predict(x_train), color = 'green')
plt.title('Salary vs Exp(Test set)')
plt.xlabel('Years of Exp')
plt.show()


m_slope = regressor.coef_
print(m_slope)

c_inter = regressor.intercept_
print(c_inter)

emp_exp_12 = m_slope*12+c_inter
print(emp_exp_12)

emp_exp_25 = m_slope*25+c_inter
print(emp_exp_25)

bias = regressor.score(x_train, y_train)
print(bias)

var = regressor.score(x_test, y_test)
print(var)

dataset.mean()
dataset['Salary'].mean()

dataset.median()
dataset['Salary'].median()

dataset.mode()
dataset['Salary'].mode()

dataset.var()

dataset.std()

dataset.corr()

dataset.describe()

dataset.skew()
dataset['Salary'].skew()

#annova ssr sst sse

y_mean = np.mean(y)
SSR = np.sum((y_pred-y_mean)**2)
print(SSR)

y = y[0:6]
SSE = np.sum((y-y_pred)**2)
print(SSE)

mean_total = np.mean(dataset.values)
SST = np.sum((dataset.values-mean_total)**2)
print(SST)

#r2
r_square = 1 - SSR/SST
print(r_square)

import pickle
filename = 'Linear_r_m.pkl'
with open(filename, 'wb') as file:
    pickle.dump(regressor, file)
print("M Work")

import os
print(os.getcwd()) 