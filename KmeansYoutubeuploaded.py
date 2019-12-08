#import the dataset from the Excel File on csv format.
#Youtube Video K means with python 2/27/2019

#import numpy, pandas and matplot

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

#Set the working Directory, so your file can be accessed and read
#You can click on the folder icon then select the path where your data is located
# Then press the python Icon and syncronize
#Finally, press F5 or run the file and it should work.


#Import sklearn Library:
from sklearn.cluster import KMeans


#Let's import the csv file
Market = pd.read_csv('Market.csv')


#Then we select just the columns wi will be working on:
X = Market.iloc[:,[1,2]].values

# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 4)

y_kmeans = kmeans.fit_predict(X)

# Visualising the clusters
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], label = 'lazy clients')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], label = 'Target clients')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], label = 'low clients')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], label = 'Premiun clients')

plt.title('CLUSTERS')
plt.xlabel('Credit Score')
plt.ylabel('Purchase in Millions')
plt.legend()
plt.show()

