import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv(r'C:\Users\Pramod\OneDrive\AI Python\Senapati Sir\Class Document\ML_All_Class\22OCT_ML\Mall_Customers.csv')
#print(dataset)

df=dataset.iloc[:,[3,4]].values
print(df)


from sklearn.cluster import  KMeans
wcss=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init='k-means++',random_state=0)
    kmeans.fit(df)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.title('the elbow method')
plt.xlabel('the number of cluster')
plt.ylabel('wcss')
plt.show()  

# kmeans=KMeans(n_clusters=5,init='k-means++',random_state=0)
# kmeans.fit_predict(df)
# print(kmeans)