#pip install --upgrade seaborn

import warnings 
import seaborn as sns
import pandas as pd
import os
import matplotlib.pyplot as plt


warnings.filterwarnings('ignore',category=FutureWarning)


# print sns get Data set names

print(sns.get_dataset_names())

#print the 'tips' data set data
tips=sns.load_dataset('tips')
print(tips.head())

#load dat set 'titanic'
titanic=sns.load_dataset('titanic')
print(titanic.head())

#set theme 

sns.set_theme(style='darkgrid')

#set excel file dataset
tips.to_csv('tips_dataset.csv',index=False)

#print the project folder path
print(os.getcwd())

#print the matplotlip figure

plt.figure(figsize=(8,6))

# 1. scatter plot
sns.scatterplot(data=tips,x='total_bill',y='tip',hue='time',size='size',palette='deep')
plt.title('ScatterPlot of the Total_bill vs Tip')
plt.show()

# 2.line plot

sns.lineplot(data=tips,x='size',y='total_bill',hue='sex',markers='o')
plt.title('LinePlot of the Total_bill ve Tip')
plt.show()


sns.lineplot(data=tips, x= 'size', y='total_bill', hue='sex',ci=None, markers='o')
plt.title("Lineplot of Total Bill vs Size")
plt.show()


print(tips.columns)

#3. bar plot

sns.barplot(data=tips, x='day', y='total_bill', hue = 'sex',palette='muted')
plt.title("Barplot of Total Bill by Day")
plt.show()

sns.boxplot(data=tips, x='day', y='tip', hue='smoker', palette='Set2')
plt.title("Boxplot of Tips by Day and Smoker Status")
plt.show()

# 5. violin plot 

sns.violinplot(data=tips, x='day', y='total_bill', hue='time', split=True, palette='pastel')
plt.title("Violin Plot of Total Bill by Day and Time")  
plt.show()


#6. count plot 

sns.countplot(data=tips, x='day', hue='smoker', palette='dark')
plt.title("Count Plot of Days by Smoker Status")
plt.show()

#7. regression plot 

sns.regplot(data=tips, x='total_bill', y='tip', scatter_kws={'s':50}, line_kws={'color':'red'})
plt.title("Regression Plot of Total Bill vs Tip")   
plt.show()


# 8. Histogram of total bill with KDE

sns.histplot(data=tips, x='total_bill', bins=20, kde=True, color='blue')
plt.title("Histogram of Total Bill with KDE")
plt.show()

#9. pairplot

sns.pairplot(tips, hue='sex', vars=["total_bill", "tip", "size"], palette='husl')
plt.suptitle("pair plot: numerberic variables by gender", y=1.02)
plt.show()


# 10 catplot 

sns.catplot(data=tips, x='day', y='tip', hue='sex', kind='point', palette='bright')
plt.title("catplot(point):Tips by day and gender")
plt.show()


# 11. jointplot

sns.jointplot(data=tips, x='total_bill', y='tip', kind='scatter', hue='smoker', color='purple', palette='coolwarm')
plt.suptitle("Jointplot: Total Bill vs Tip", y=1.02)
plt.show()


# 11. jointplot

sns.jointplot(data=tips, x='total_bill', y='tip', kind='scatter', hue='smoker',  palette='coolwarm')
plt.suptitle("Jointplot: Total Bill vs Tip", y=1.02)
plt.show()

# Facetgrid 

g = sns.FacetGrid(tips, col='time', row='smoker', margin_titles=True).map(sns.histplot, 'total_bill', bins=20, kde=True).add_legend()
g


#13. strip plot

sns.stripplot(data=tips, x='day', y='tip', hue='sex', jitter=True, palette='Set1')
plt.title("strip plot: Tips by data and gender")
plt.show()