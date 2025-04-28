# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis

# Load sample social media data (You can replace this with your dataset)
data = pd.DataFrame({
    'user_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'followers_count': [100, 200, 350, 150, 500, 120, 60, 300, 400, 800],
    'likes': [10, 15, 10, 25, 30, 50, 45, 60, 100, 75],
    'shares': [5, 3, 7, 8, 6, 12, 10, 9, 15, 18],
    'comments': [1, 2, 3, 4, 5, 6, 2, 3, 6, 10],
    'engagement_rate': [0.1, 0.15, 0.2, 0.18, 0.3, 0.25, 0.28, 0.35, 0.4, 0.5],
    'sentiment_score': [0.8, 0.5, 0.7, 0.9, 0.6, 0.4, 0.6, 0.8, 0.9, 0.7]
})

# Display the first few rows of the data
print("First 5 rows of data:")
print(data.head())

# Descriptive Statistics
print("\nDescriptive Statistics:")
print(data.describe())

# Central Tendency Measures
print("\nMean of Followers Count:", data['followers_count'].mean())
print("Median of Followers Count:", data['followers_count'].median())
print("Mode of Followers Count:", data['followers_count'].mode()[0])

# Dispersion Measures
print("\nStandard Deviation of Followers Count:", data['followers_count'].std())
print("Variance of Followers Count:", data['followers_count'].var())
print("Range of Followers Count:", data['followers_count'].max() - data['followers_count'].min())

# Interquartile Range (IQR)
Q1 = data['followers_count'].quantile(0.25)
Q3 = data['followers_count'].quantile(0.75)
IQR = Q3 - Q1
print("\nInterquartile Range (IQR) of Followers Count:", IQR)

# Skewness and Kurtosis
print("\nSkewness of Followers Count:", skew(data['followers_count']))
print("Kurtosis of Followers Count:", kurtosis(data['followers_count']))

# Data Quality - Checking for Missing Values
print("\nMissing Values in each column:")
print(data.isnull().sum())

# -----------------------------------
# Visualizations

# Set plot style
sns.set(style="whitegrid")

# Plot 1: Histogram and Boxplot
plt.figure(figsize=(14, 8))

# Histogram of Followers Count
plt.subplot(2, 2, 1)
sns.histplot(data['followers_count'], kde=True, color='skyblue', bins=10)
plt.title('Distribution of Followers Count')
plt.xlabel('Followers Count')
plt.ylabel('Frequency')

# Boxplot of Followers Count
plt.subplot(2, 2, 2)
sns.boxplot(x=data['followers_count'], color='lightgreen')
plt.title('Boxplot of Followers Count')
plt.xlabel('Followers Count')

plt.tight_layout()
plt.show()

# Plot 2: Heatmap of Correlations
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Heatmap')
plt.show()
