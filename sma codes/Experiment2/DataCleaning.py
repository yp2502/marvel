import pandas as pd
import numpy as np

file_path = 'icc_fb_page.csv'

# Load the dataset
df = pd.read_csv(file_path)
print("Dataset Overview:")
print(df.info())
print("\nFirst few rows of the dataset:")
print(df.head())

# 1. Handling missing values
# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Drop rows with missing values in the 'text' column
df.dropna(subset=['text'], inplace=True)

# Check if missing values were handled
print("\nMissing values after handling:")
print(df.isnull().sum())

# 2. Remove duplicate rows
# Number of rows initially without cleaning
print("\nNumber of rows before removing duplicates:", df.shape[0])

# Remove duplicate rows
df.drop_duplicates(inplace=True)
print("\nNumber of rows after removing duplicates:", df.shape[0])

# 3. Standardizing text columns (e.g., the 'text' column)
df['text'] = df['text'].str.strip() # Remove extra spaces from the 'text' column
df['text'] = df['text'].str.lower() # Convert the 'text' column to lowercase

# 4. Handling outliers (if any)
threshold = 1000 # Set your threshold for 'likes'

df = df[df['likes'] <= threshold] # Remove rows where 'likes' exceed the threshold
# Drop columns like 'comments' and any other irrelevant columns

df.drop(columns=['comments', 'shares'], inplace=True) # Adjust according to your needs

# 7. Check data types after cleaning
print("\nData types after cleaning:")
print(df.dtypes)

# Save the cleaned data to a new CSV file
df.to_csv('icc_fb_page_cleaned.csv', index=False)
print("\nData cleaning complete. Cleaned data saved as 'icc_fb_page_cleaned.csv'.")
