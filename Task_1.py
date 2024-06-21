import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

matches = pd.read_csv('D:\Intern\Task1\matches.csv')
deliveries = pd.read_csv('D:\Intern\Task1\deliveries.csv')

print("Matches Dataset Columns:", matches.columns)
print(matches.head())

print("Deliveries Dataset Columns:", deliveries.columns)
print(deliveries.head())

plt.figure(figsize=(12, 8))
sns.countplot(y='winner', data=matches, order=matches['winner'].value_counts().index, palette='viridis')
plt.title('Number of Wins per Team in IPL')
plt.xlabel('Count')
plt.ylabel('Teams')
plt.show()

if 'batter' in deliveries.columns:
    total_runs = deliveries.groupby('batter')['batsman_runs'].sum().reset_index()
    total_runs = total_runs.sort_values(by='batsman_runs', ascending=False)
    plt.figure(figsize=(12, 8))
    sns.histplot(total_runs['batsman_runs'], bins=30, kde=True, color='blue')
    plt.title('Histogram of Total Runs Scored by Players in IPL')
    plt.xlabel('Total Runs')
    plt.ylabel('Frequency')
    plt.show()
else:
    print("Column 'batter' does not exist in deliveries dataset.")
