import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dataset=pd.read_csv(r'C:\Users\Pramod\OneDrive\AI Python\Senapati Sir\Class Document\ML_All_Class\8OCT_ML\Salary_Data.csv')


x = dataset.iloc[:, :-1]  
y = dataset.iloc[:, -1] 


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, 
                                                    test_size=0.20,
                                                    random_state=0) 

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train) 

y_pred = regressor.predict(x_test) 

# Compare predicted and actual salaries from the test set
comparison = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(comparison) 

plt.scatter(x_test, y_test, color = 'red')  # Real salary data (testing)
plt.plot(x_train, regressor.predict(x_train), color = 'blue')  # Regression line from training set
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary') 
plt.show()  

m_slope = regressor.coef_ 
print(m_slope)


c_inter = regressor.intercept_
print(c_inter) 

emp_exp_12 = m_slope*12+c_inter
print(emp_exp_12) 

emp_exp_20 = m_slope*20+c_inter
print(emp_exp_20) 