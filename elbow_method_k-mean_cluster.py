# -*- coding: utf-8 -*-
"""lab_task_N1_221-15-5013.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XiD8YNK2wz5Y2o814_GizJc8SO9sughC
"""

#dataset sourse link
import kagglehub
path = kagglehub.dataset_download("jainaru/thyroid-disease-data")
print("Path to dataset files:", path)

#import library
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import OneHotEncoder

#Upload dataset
dataset = pd.read_csv('Thyroid_Diff.csv')
dataset

#Check null value
nullvalue = dataset.isnull().sum()
print(nullvalue)

#Preprocessing and covert categorical value into numerical value
num_col = ['Age']
cat_col = dataset.columns.drop('Age')

encoder = OneHotEncoder(sparse_output=False)
encoded_cat = encoder.fit_transform(dataset[cat_col])
encoded_cat_dataset = pd.DataFrame(encoded_cat, columns=encoder.get_feature_names_out(cat_col))
numeric_dataset = pd.concat([dataset[num_col], encoded_cat_dataset], axis=1)
dataset = numeric_dataset
dataset

# List to store inertia values for each K
inertia = []

for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)

    kmeans.fit(numeric_dataset)

    inertia.append(kmeans.inertia_)

print(inertia)

# Plotting the Elbow Curve
plt.figure(figsize=(8,5))
plt.plot(range(1, 11), inertia, marker='o', linestyle='--')
plt.title('Elbow Method for Optimal K')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia (Sum of Squared Distances)')
plt.show()