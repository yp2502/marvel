


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, StandardScaler
from scipy.stats import skew, kurtosis
df = pd.read_csv('datacleaning.csv')

print("Initial Data:")
print(df.info())
print(df.head(11))

# Handling missing values
num_imputer = SimpleImputer(strategy="mean")  # For numerical columns
cat_imputer = SimpleImputer(strategy="most_frequent")  # For categorical columns

for col in df.select_dtypes(include=['number']).columns:
    df[col] = num_imputer.fit_transform(df[[col]])
for col in df.select_dtypes(include=['object']).columns:
    # Use df[col] to get a Series instead of df[[col]] to get a DataFrame
    df[col] = cat_imputer.fit_transform(df[col].values.reshape(-1, 1))[:, 0]

# Display data after handling missing values
print("\nData after handling missing values:")
print(df.info())
print(df.head(11))

df.drop_duplicates(inplace=True)

print("\nData after removing duplicates:")
print(df.info())
print(df.head(11))

# Handling outliers using IQR for numerical features only
numerical_cols = df.select_dtypes(include=['number']).columns

Q1 = df[numerical_cols].quantile(0.25)
Q3 = df[numerical_cols].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter outliers only for numerical features
df = df[~((df[numerical_cols] < lower_bound) | (df[numerical_cols] > upper_bound)).any(axis=1)]

print("\nData after handling outliers:")
print(df.info())
print(df.head(11))

encoder = LabelEncoder()
for col in df.select_dtypes(include=['object']).columns:
    df[col] = encoder.fit_transform(df[col])

print("\nData after encoding categorical variables:")
print(df.info())
print(df.head(11))

if 'joining date' in df.columns:
    df['joining date'] = pd.to_datetime(df['joining date'], errors='coerce')

print("\nFinal cleaned data:")
print(df.info())
print(df.head(11))

df.to_csv("cleaned_data.csv", index=False)
print("\nData cleaning completed. Cleaned dataset saved as 'cleaned_data.csv'.")

from google.colab import drive
drive.mount('/content/drive')