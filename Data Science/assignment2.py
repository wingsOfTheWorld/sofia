import seaborn
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler


"""
Data Munging
Data munging is the process of turning a data set with a bunch of junk in it into a nice clean data set.

Data Wrangling
Data cleaning refers to the process of processing raw data to make it more suitable for analysis.

Data Cleaning
Data cleaning is a subset of the data wrangling process that focuses on identifying and correcting errors, 
inconsistencies, and anomalies in the data.

Data Transformation
Data transformation refers to the process of structurally altering or converting data to make it more suitable for 
specific analytical needs or models.
"""

# 1. Load the dataset into an pandas dataframe.
iris_df = seaborn.load_dataset('iris')
print(iris_df.head())

# 2.Based on the concepts learned in Chapter 6, check for any missing values in the dataset.
# If there are, handle them appropriately.
if iris_df.isna().values.any():
    print('This data set has missing values.')
else:
    print('This data set has no missing values.')

# 3.Detect and resolve any duplicate entries in the dataset.
duplicate_entries = iris_df.duplicated()  # Detect duplicate entries
print(iris_df[duplicate_entries])  # show duplicate entries
iris_df = iris_df.drop_duplicates()  # delete duplicate entries

# 4.Create a new column called Petal.Ratio, which is the ratio of Petal.Length to LengthPetal.Width
iris_df['petal_ratio'] = iris_df['petal_length'] / iris_df['petal_width']
print(iris_df['petal_ratio'])

# 5.Normalize the column using a suitable method (e.g., min-max normalization, z-score normalization, etc.).Petal.Length
# min-max normalization
minmax_scaler = MinMaxScaler()
iris_df['petal_length_minmax'] = minmax_scaler.fit_transform(iris_df[['petal_length']])
print(iris_df['petal_length_minmax'])

# z-score normalization
zscore_scaler = StandardScaler()
iris_df['petal_length_zscore'] = zscore_scaler.fit_transform(iris_df[['petal_length']])
print(iris_df['petal_length_zscore'])

# create scatter
plt.scatter(range(len(iris_df['petal_length'])), iris_df['petal_length'], alpha=0.5)
plt.title('Scatter Plot of Petal Length')
plt.xlabel('Index')
plt.ylabel('Petal Length')
plt.show()

"""
conclusion: as the scatter show, there are some outliers in the data set, so that I think z-score normalization is 
more suitable.
"""
