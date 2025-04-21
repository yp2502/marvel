

import pandas as pd
import scipy.stats as stats

df = pd.read_excel('/content/exp3_RelianceDataMart.xlsx')

print("Initial Data:")
print(df.info())
print(df.head(11))

# Assuming the 'Rice Bag' values are in a column named 'Rice_Bag'
column_name = 'Rice_Bag_Weight'  # Change if needed

# Check if column exists
if column_name not in df.columns:
    raise ValueError(f"Column '{column_name}' not found in dataset.")

# Drop NaN values if any
df = df.dropna(subset=[column_name])

# Hypothesized population mean (change this as needed)
population_mean = 25 # Example value

# Perform One-Sample t-test
t_stat, p_value = stats.ttest_1samp(df[column_name], population_mean)

# Display results
print("\nOne-Sample t-test Results:")
print(f"T-Statistic: {t_stat}")
print(f"P-Value: {p_value}")

# Conclusion based on p-value
alpha = 0.05  # Significance level
if p_value < alpha:
    print("Result: Reject the null hypothesis (Significant difference found).")
else:
    print("Result: Fail to reject the null hypothesis (No significant difference found).")

# Statistical Calculations
mean_value = df[column_name].mean()
median_value = df[column_name].median()
mode_value = df[column_name].mode()[0]
max_value = df[column_name].max()
min_value = df[column_name].min()
std_dev = df[column_name].std()
std_error = stats.sem(df[column_name])
kurtosis_value = stats.kurtosis(df[column_name])
skewness_value = stats.skew(df[column_name])
range_value = max_value - min_value
sum_value = df[column_name].sum()
count_value = df[column_name].count()

# Display statistical values
print("\nDescriptive Statistics:")
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
print(f"Max Value: {max_value}")
print(f"Min Value: {min_value}")
print(f"Standard Deviation: {std_dev}")
print(f"Standard Error: {std_error}")
print(f"Kurtosis: {kurtosis_value}")
print(f"Skewness: {skewness_value}")
print(f"Range: {range_value}")
print(f"Sum: {sum_value}")
print(f"Count: {count_value}")

# Hypothesized population mean
population_mean = 25  # Updated as per request

# Perform One-Sample t-test
t_stat, p_value = stats.ttest_1samp(df[column_name], population_mean)

# T Critical Value
alpha = 0.05
degrees_of_freedom = count_value - 1
t_critical = stats.t.ppf(1 - alpha / 2, degrees_of_freedom)

# Display results
print("\nOne-Sample t-test Results:")
print(f"T-Statistic: {t_stat}")
print(f"P-Value: {p_value}")
print(f"T Critical Value: {t_critical}")

# Conclusion based on p-value
if p_value < alpha:
    print("Result: Reject the null hypothesis (Significant difference found).")
else:
    print("Result: Fail to reject the null hypothesis (No significant difference found).")

import pandas as pd
import scipy.stats as stats

# Load Pre-Post Score dataset
pre_post_file = "/content/exp3_Pre_Post_Score.xlsx"
pre_post_df = pd.read_excel(pre_post_file)

# Display first few rows to inspect the data
print("Pre-Post Score Data:")
print(pre_post_df.head())

# Assuming 'Pre_Score' and 'Post_Score' are the correct column names
pre_col, post_col = 'Pre_Score', 'Post_Score'
if pre_col not in pre_post_df.columns or post_col not in pre_post_df.columns:
    raise ValueError("Pre_Score or Post_Score column not found in dataset.")

# Drop NaN values if any
pre_post_df = pre_post_df.dropna(subset=[pre_col, post_col])

# Compute statistics
mean_pre = pre_post_df[pre_col].mean()
mean_post = pre_post_df[post_col].mean()
var_pre = pre_post_df[pre_col].var()
var_post = pre_post_df[post_col].var()
n = pre_post_df.shape[0]  # Number of observations
pearson_corr = pre_post_df[pre_col].corr(pre_post_df[post_col])
hypo_mean_diff = 0  # Hypothesized mean difference
df = n - 1  # Degrees of freedom

# Perform Paired Sample t-test
t_stat, p_value_two_tail = stats.ttest_rel(pre_post_df[pre_col], pre_post_df[post_col])
p_value_one_tail = p_value_two_tail / 2

# T Critical Values
alpha = 0.05
t_critical_one_tail = stats.t.ppf(1 - alpha, df)
t_critical_two_tail = stats.t.ppf(1 - alpha / 2, df)

# Display results
print("\nPaired Sample T-Test Results:")
print(f"Mean Pre-Score: {mean_pre}")
print(f"Mean Post-Score: {mean_post}")
print(f"Variance Pre-Score: {var_pre}")
print(f"Variance Post-Score: {var_post}")
print(f"Number of Observations: {n}")
print(f"Pearson Correlation: {pearson_corr}")
print(f"Hypothesized Mean Difference: {hypo_mean_diff}")
print(f"Degrees of Freedom: {df}")
print(f"T-Statistic: {t_stat}")
print(f"P-Value (One-Tail): {p_value_one_tail}")
print(f"T Critical Value (One-Tail): {t_critical_one_tail}")
print(f"P-Value (Two-Tail): {p_value_two_tail}")
print(f"T Critical Value (Two-Tail): {t_critical_two_tail}")

# Conclusion based on p-value
if p_value_two_tail < alpha:
    print("Result: Reject the null hypothesis (Significant difference found).")
else:
    print("Result: Fail to reject the null hypothesis (No significant difference found).")

