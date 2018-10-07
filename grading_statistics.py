# Script for calculating grading statistics for Piazza

import pandas as pd

# Read CSV into dataframe

csv_name = input("Input CSV filename:\n")
df = pd.read_csv(csv_name)

# Calculate statistics

points_possible = df['Total Points Possible'].median()
n = df['Total Points'].count()
min = df['Total Points'].min() / points_possible * 100
q1 = df['Total Points'].quantile(.25) / points_possible * 100
q2 = df['Total Points'].quantile(.50) / points_possible * 100
q3 = df['Total Points'].quantile(.75) / points_possible * 100
max = df['Total Points'].max() / points_possible * 100
mean = df['Total Points'].mean() / points_possible * 100
stdev = df['Total Points'].std() / points_possible * 100

# Print statistics with formatting for Piazza

print("N : ", n)
print("Min : ", round(min,2), "%")
print("Q1 : ", round(q1,2), "%")
print("Q2 / Median : ", round(q2,2), "%")
print("Q3 : ", round(q3,2), "%")
print("Max : ", round(max,2), "%")
print("Mean : ", round(mean,2), "%")
print("Stdev : ", round(stdev,2), "%")
