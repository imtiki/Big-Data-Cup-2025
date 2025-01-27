import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"shift_data.csv")
Y = df.drop(columns = ['Time into Shift', 'Players'])
Y = Y.div(df['Players'], axis = 0)
Y = Y.div(60)
df['Shift Score'] = (Y['Goals'] + (0.8 * Y['Takeaways']) + (0.20 * Y['Puck Recoveries'])
                     - (0.50 * Y['Penalty']) - (0.50 * Y['Incomplete Plays']) + (0.50 * Y['Plays'])
                     + (0.10 * Y['Shots']))
df_for_plot = df[(df["Time into Shift"] < 121)]
for col in df_for_plot.columns.tolist():
     sns.scatterplot(x = df_for_plot['Time into Shift'], y = df_for_plot[col], c = "purple")
     plt.xlabel('Number of Seconds into Shift')
     plt.ylabel(col + ' ' + "per 60 per shift")
     plt.title(col + ' ' + "per 60 per shift by Number of Seconds into Shift")
     plt.show()