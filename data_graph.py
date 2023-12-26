import pandas as pd
import matplotlib.pyplot as plt

# Data
df = pd.DataFrame({
    'Game': ['Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7', 'Game 8', 'Game 9', 'Game 10', 'Game 11', 'Game 12', 'Game 13', 'Game 14', 'Game 15', 'Game 16', 'Game 17', 'Game 18', 'Game 19', 'Game 20'],
    'Game Length (sec)': [2878, 2252, 1982, 1280, 1703, 1589, 2378, 1995, 1751, 1861, 1533, 2331, 1533, 1361, 147, 1796, 1411, 1567, 1466, 2028],
    'Kills': [7, 8, 5, 2, 2, 3, 16, 16, 5, 2, 0, 9, 3, 0, 0, 12, 5, 3, 4, 2],
    'Deaths': [10, 7, 4, 7, 2, 10, 6, 6, 7, 9, 7, 4, 5, 3, 0, 4, 8, 2, 7, 6],
    'Assists': [9, 7, 3, 1, 3, 3, 4, 7, 3, 2, 1, 9, 0, 4, 0, 5, 2, 9, 5, 3],
    'Gold Earned': [18206, 17202, 16022, 8084, 10760, 9177, 21350, 18669, 9973, 11192, 6887, 18140, 9806, 8275, 761, 17027, 8502, 9500, 7877, 12336],
    'CS': [285, 281, 299, 146, 247, 163, 289, 251, 175, 199, 145, 266, 186, 163, 11, 239, 64, 169, 128, 75],
    'Damage to Champions': [37145, 38409, 20746, 15283, 20056, 18175, 39527, 89553, 28667, 18167, 9598, 42410, 20383, 7956, 628, 33597, 9083, 12221, 12770, 12705]
})

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(df['Game'], df['Game Length (sec)'], label='Game Length')
plt.plot(df['Game'], df['Kills'], label='Kills')
plt.plot(df['Game'], df['Deaths'], label='Deaths')
plt.plot(df['Game'], df['Assists'], label='Assists')
plt.plot(df['Game'], df['Gold Earned'], label='Gold Earned')
plt.plot(df['Game'], df['CS'], label='CS')
plt.plot(df['Game'], df['Damage to Champions'], label='Damage to Champions')

# Setting the labels and title
plt.xlabel('Games')
plt.ylabel('Statistics')
plt.title('Ranked Game Statistics')
plt.xticks(rotation=45)

# Displaying the legend and showing the plot
plt.legend()
plt.tight_layout()
plt.show()
