import csv
import pandas as pd
import matplotlib.pyplot as plt


#datasets

dc_events = "2024-11-15.Team.D.@.Team.C.-.Events.csv"
dc_shifts = "2024-11-15.Team.D.@.Team.C.-.Shifts.csv"
fe_events = "2024-11-16.Team.F.@.Team.E.-.Events.csv"
fe_shifts = "2024-11-16.Team.F.@.Team.E.-.Shifts.csv"
hg_events = "2024-10-25.Team.H.@.Team.G.-.Events.csv"
hg_shifts = "2024-10-25.Team.H.@.Team.G.-.Shifts.csv"



def to_seconds(x):
    colo = x.find(":")
    mins_str = x[0:colo]
    mins = int(mins_str)
    sec_str = x[colo+1:]
    secs = int(sec_str)
    return (mins * 60) + secs


def find_possession_changes(csvfile):
    home = {'gains': [], 'lose': []}
    away = {'gains': [], 'lose': []}
    with open(csvfile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                home_team_has_puck = False
                puck_loose = True
                line_count += 1
            elif row[5] != row[6]:
                line_count += 1
            else:
                time = row[3], to_seconds(row[4])

                if line_count == 1:
                    home_team = row[1]
                    away_team = row[2]
                if row[11] == 'Faceoff Win':
                    if row[9] == home_team:
                        if not home_team_has_puck and not puck_loose:
                            if row[4] == '20:00':
                                away['lose'].append((str(int(row[3])-1), 0))
                            else:
                                away['lose'].append(time)
                        elif not puck_loose:
                            if row[4] == '20:00':
                                home['lose'].append((str(int(row[3])-1), 0))
                            else:
                                home['lose'].append(time)
                        home_team_has_puck = True
                        home['gains'].append(time)
                    else:
                        if home_team_has_puck and not puck_loose:
                            if row[4] == '20:00':
                                home['lose'].append((str(int(row[3])-1), 0))
                            else:
                                home['lose'].append(time)
                        elif not puck_loose:
                            if row[4] == '20:00':
                                away['lose'].append((str(int(row[3])-1), 0))
                            else:
                                away['lose'].append(time)
                        home_team_has_puck = False
                        away['gains'].append(time)
                    puck_loose = False

                elif row[11] == 'Incomplete Play':
                    puck_loose = True
                    if row[9] == home_team:
                        home['lose'].append(time)
                    elif row[9] == away_team:
                        away['lose'].append(time)

                elif row[11] == 'Zone Entry' and row[14] == 'Dumped':
                    puck_loose = True
                    if row[9] == home_team:
                        home['lose'].append(time)
                    elif row[9] == away_team:
                        away['lose'].append(time)

                elif row[11] == 'Dump In/Out':
                    puck_loose = True
                    if row[9] == home_team:
                        home['lose'].append(time)
                    elif row[9] == away_team:
                        away['lose'].append(time)

                elif row[11] == 'Takeaway':
                    puck_loose = False
                    if row[9] == away_team:
                        home_team_has_puck = False
                        away['gains'].append(time)
                    else:
                        home_team_has_puck = True
                        home['gains'].append(time)

                elif row[11] == 'Shot':
                    puck_loose = True
                    if row[9] == home_team:
                        home['lose'].append(time)
                    elif row[9] == away_team:
                        away['lose'].append(time)

                elif row[11] == 'Puck Recovery':
                    if puck_loose and row[9] == home_team:
                        home_team_has_puck = True
                        home['gains'].append(time)
                        puck_loose = False
                    elif puck_loose and row[9] == away_team:
                        home_team_has_puck = False
                        away['gains'].append(time)
                        puck_loose = False
                    elif row[9] == home_team and not home_team_has_puck:
                        home_team_has_puck = True
                        away['lose'].append(time)
                        home['gains'].append(time)
                    elif row[9] == away_team and home_team_has_puck:
                        home_team_has_puck = False
                        home['lose'].append(time)
                        away['gains'].append(time)
                line_count += 1
    events = {home_team: home, away_team: away}
    return events


def get_team_shifts(csvfile):
    with open(csvfile) as csv_file:
        shifts = csv.reader(csv_file, delimiter=',')
        line_count = 0
        shift_dict = {}
        for row in shifts:
            if line_count == 0:
                line_count += 1
            elif row[3] == 'Go':
                line_count += 1
            else:
                rand = False
                for thing in shift_dict:
                    if thing == row[2]:
                        rand = True
                if rand:
                    rand1 = False
                    for thing in shift_dict[row[2]]:
                        if thing == row[3]:
                            rand1 = True
                    if rand1:
                        shift_dict[row[2]][row[3]].append((row[5], to_seconds(row[6]), to_seconds(row[7])))
                    else:
                        shift_dict[row[2]].update({row[3]: [(row[5], to_seconds(row[6]), to_seconds(row[7]))]})
                else:
                    shift_dict.update({row[2]: {row[3]: [(row[5], to_seconds(row[7]), to_seconds(row[7]))]}})

    return shift_dict


def get_who_on_ice_at_moment(game_shifts, game_happening, team1, team2):
    length = {'gains': {}, 'loses': {}}
    for i in range(0, 250):
        length['gains'].update({i: 0})
        length['loses'].update({i: 0})
    # split dicts by team
    team1s = game_shifts[team1]
    team2s = game_shifts[team2]
    team1e = game_happening[team1]
    team2e = game_happening[team2]
    for i in range(0, len(team1e['lose'])):
        for player in team1s:
            for j in range(0, len(team1s[player])):
                if team1e['lose'][i][0] == team1s[player][j][0] and team1s[player][j][2] <= team1e['lose'][i][1] <= team1s[player][j][1]:
                    rand_time = team1e['lose'][i][1] - team1s[player][j][2]
                    length['loses'][rand_time] += 1
    for i in range(0, len(team2e['lose'])):
        for player in team2s:
            for j in range(0, len(team2s[player])):
                if team2e['lose'][i][0] == team2s[player][j][0] and team2s[player][j][2] <= team2e['lose'][i][1] <= team2s[player][j][1]:
                    rand_time = team2e['lose'][i][1] - team2s[player][j][2]
                    length['loses'][rand_time] += 1
    for i in range(0, len(team2e['gains'])):
        for player in team2s:
            for j in range(0, len(team2s[player])):
                if team2e['gains'][i][0] == team2s[player][j][0] and team2s[player][j][2] <= team2e['gains'][i][1] <= team2s[player][j][1]:
                    rand_time = team2e['gains'][i][1] - team2s[player][j][2]
                    length['gains'][rand_time] += 1

    for i in range(0, len(team1e['gains'])):
        for player in team1s:
            for j in range(0, len(team1s[player])):
                if team1e['gains'][i][0] == team1s[player][j][0] and team1s[player][j][2] <= team1e['gains'][i][1] <= team1s[player][j][1]:
                    rand_time = team1e['gains'][i][1] - team1s[player][j][2]
                    length['gains'][rand_time] += 1
    return length


real_dc_shifts = get_team_shifts(dc_shifts)
real_dc_events = find_possession_changes(dc_events)
real_fe_events = find_possession_changes(fe_events)
real_fe_shifts = get_team_shifts(fe_shifts)
real_hg_events = find_possession_changes(hg_events)
real_hg_shifts = get_team_shifts(hg_shifts)

last_list = {}
# blah.csv is a dictionary of shift time and shifts.
players = open("blah.csv")
csv_reader = csv.reader(players, delimiter=',')
row_count = 0
for row in csv_reader:
    if row_count == 0:
        last_list.update({0: 0})
        row_count += 1
    else:
        last_list.update({int(row[0]): int(row[1])})


l1 = get_who_on_ice_at_moment(real_dc_shifts, real_dc_events, 'Team D', 'Team C')
l2 = get_who_on_ice_at_moment(real_fe_shifts, real_fe_events, 'Team F', 'Team E')
l3 = get_who_on_ice_at_moment(real_hg_shifts, real_hg_events, 'Team H', 'Team G')

final_dict = {'gains': {}, 'loses': {}}
freq_dict = {'gains': {}, 'loses': {}}
for i in range(1, 214):
    total_gains = l1['gains'][i] + l2['gains'][i] + l3['gains'][i]
    total_loses = l1['loses'][i] + l2['loses'][i] + l3['loses'][i]
    final_dict['gains'][i] = (total_gains / last_list[i] / i / 60)
    final_dict['loses'][i] = (total_loses / last_list[i] / i / 60)
    freq_dict['gains'][i] = (total_gains / i / 60)
    freq_dict['loses'][i] = (total_loses / i / 60)

x = final_dict['loses'].keys()
y = final_dict['loses'].values()

plt.scatter(x, y)

plt.title("Team Possession Loss per 60 by Number of Seconds into Shift")
plt.xlabel("Shift Length")
plt.ylabel("Team Possession Loss per 60 per shift")

plt.show()


