import pandas as pd
from Tidy import dc_events, dc_shifts, dc_tracking, hg_events, hg_shifts, fe_shifts,fe_events



df_dict = {i: {'Shots': 0, 'Plays':0,
                             'Incomplete Plays':0, 'Goals':0, 'Takeaways':0, 'Penalty':0,
                             'Puck Recoveries':0, 'Skating Speed' :0, 'Players':0} for i in range(1, 215)}

for team in ["Team C", "Team D"]:
    team_df = dc_shifts[dc_shifts['team_name'] == team]
    for (i, num), matching_row in team_df.groupby(["Player_Id", "shift_number"]):
        start = matching_row['start_clock'].iloc[0]
        end = matching_row['end_clock'].iloc[0]
        total = matching_row['shift_length'].iloc[0]
        events_in_shift = dc_events[(dc_events['Clock'] <= start) & (dc_events['Clock'] >= end)
                                    & (dc_events['Player_Id'] == i) & (dc_events['Team'] == team)
        & (dc_events['Home_Team_Skaters'] == 5) & (dc_events['Away_Team_Skaters'] == 5)]
        for l in range(1, total):
            if 1 <= l <= 214:
                df_dict[l]['Players'] += 1
        for index, row in events_in_shift.iterrows():
            k = start - row['Clock']
            if total <= 214 and 0 < k:
                if row['Event'] == 'Shot':
                    if row['Detail_2'] == 'Blocked' or row['Detail_2'] == 'On Net':
                        for j in range(k, total):
                            df_dict[j]['Shots'] += 1/j
                elif row['Event'] == 'Play':
                    for j in range(k, total):
                        df_dict[j]['Plays'] += 1/j
                elif row['Event'] == 'Incomplete Play':
                    for j in range(k, total):
                        df_dict[j]['Incomplete Plays'] += 1/j
                elif row['Event'] == 'Puck Recovery':
                    for j in range(k, total):
                        df_dict[j]['Puck Recoveries'] += 1/j
                elif row['Event'] == 'Takeaway':
                    for j in range(k, total):
                        df_dict[j]['Takeaways'] += 1/j
                elif row['Event'] == 'Goal':
                    for j in range(k, total):
                        df_dict[j]['Goals'] += 1/j
                elif row['Event'] == 'Penalty Taken':
                    for j in range(k, total):
                        df_dict[j]['Penalty'] += 1/j

for team in ["Team E", "Team F"]:
   team_df = fe_shifts[fe_shifts['team_name'] == team]
   for (i, num), matching_row in team_df.groupby(["Player_Id", "shift_number"]):
       start = matching_row['start_clock'].iloc[0]
       end = matching_row['end_clock'].iloc[0]
       total = matching_row['shift_length'].iloc[0]
       events_in_shift = fe_events[(fe_events['Clock'] <= start) & (fe_events['Clock'] >= end)
                                   & (fe_events['Player_Id'] == i) & (fe_events['Team'] == team)
       & (dc_events['Home_Team_Skaters'] == 5) & (dc_events['Away_Team_Skaters'] == 5)]
       for l in range(1, total):
           if 1 <= l <= 214:
               df_dict[l]['Players'] += 1
       for index, row in events_in_shift.iterrows():
           k = start - row['Clock']
           if total <= 214 and 0 < k:
               if row['Event'] == 'Shot':
                   if row['Detail_2'] == 'Blocked' or row['Detail_2'] == 'On Net':
                       for j in range(k, total):
                           df_dict[j]['Shots'] += 1/j
               elif row['Event'] == 'Play':
                   for j in range(k, total):
                       df_dict[j]['Plays'] += 1/j
               elif row['Event'] == 'Incomplete Play':
                   for j in range(k, total):
                       df_dict[j]['Incomplete Plays'] += 1/j
               elif row['Event'] == 'Puck Recovery':
                   for j in range(k, total):
                       df_dict[j]['Puck Recoveries'] += 1/j
               elif row['Event'] == 'Takeaway':
                   for j in range(k, total):
                       df_dict[j]['Takeaways'] += 1/j
               elif row['Event'] == 'Goal':
                   for j in range(k, total):
                       df_dict[j]['Goals'] += 1/j
               elif row['Event'] == 'Penalty Taken':
                   for j in range(k, total):
                       df_dict[j]['Penalty'] += 1/j
for team in ["Team H", "Team G"]:
   team_df = hg_shifts[hg_shifts['team_name'] == team]
   for (i, num), matching_row in team_df.groupby(["Player_Id", "shift_number"]):
       start = matching_row['start_clock'].iloc[0]
       end = matching_row['end_clock'].iloc[0]
       total = matching_row['shift_length'].iloc[0]
       events_in_shift = hg_events[(hg_events['Clock'] <= start) & (hg_events['Clock'] >= end)
                                   & (hg_events['Player_Id'] == i) & (hg_events['Team'] == team)
       & (dc_events['Home_Team_Skaters'] == 5) & (dc_events['Away_Team_Skaters'] == 5)]
       for l in range(1, total):
           if 1 <= l <= 214:
               df_dict[l]['Players'] += 1
       for index, row in events_in_shift.iterrows():
           k = start - row['Clock']
           if total <= 214 and 0 < k:
               if row['Event'] == 'Shot':
                   if row['Detail_2'] == 'Blocked' or row['Detail_2'] == 'On Net':
                       for j in range(k, total):
                           df_dict[j]['Shots'] += 1/j
               elif row['Event'] == 'Play':
                   for j in range(k, total):
                       df_dict[j]['Plays'] += 1/j
               elif row['Event'] == 'Incomplete Play':
                   for j in range(k, total):
                       df_dict[j]['Incomplete Plays'] += 1/j
               elif row['Event'] == 'Puck Recovery':
                   for j in range(k, total):
                       df_dict[j]['Puck Recoveries'] += 1/j
               elif row['Event'] == 'Takeaway':
                   for j in range(k, total):
                       df_dict[j]['Takeaways'] += 1/j
               elif row['Event'] == 'Goal':
                   for j in range(k, total):
                       df_dict[j]['Goals'] += 1/j
               elif row['Event'] == 'Penalty Taken':
                   for j in range(k, total):
                       df_dict[j]['Penalty'] += 1/j


df = pd.DataFrame.from_dict(df_dict, orient = 'index')
df = df.reset_index()
df.rename(columns = {'index':'Time into Shift'}, inplace = True)
blah = df[['Time into Shift', 'Players']]

df.to_csv("shift_data.csv", index = False)
blah.to_csv("blah.csv", index = False)