import pandas as pd



dc_tracking = pd.read_csv(r"data\2024-11-15.Team.D.@.Team.C.-.Tracking.csv", dtype={'Column_9': str})
dc_tracking.replace({'n/a': '', 'Go': ''}, inplace=True)
dc_tracking.to_csv(r"data\new_2024-11-15.Team.D.@.Team.C.-.Tracking.csv", index = False)


fe_tracking = pd.read_csv(r"data\2024-11-16.Team.F.@.Team.E.-.Tracking.csv", dtype={'Column_9': str})


dc_events = pd.read_csv(r"data\2024-11-15.Team.D.@.Team.C.-.Events.csv")
dc_shifts = pd.read_csv(r"data\2024-11-15.Team.D.@.Team.C.-.Shifts.csv")
fe_events = pd.read_csv(r"data\2024-11-16.Team.F.@.Team.E.-.Events.csv")
fe_shifts = pd.read_csv(r"data\2024-11-16.Team.F.@.Team.E.-.Shifts.csv")
hg_events = pd.read_csv(r"data\2024-10-25.Team.H.@.Team.G.-.Events.csv")
hg_shifts = pd.read_csv(r"data\2024-10-25.Team.H.@.Team.G.-.Shifts.csv")

hg_tracking = pd.read_csv(r"data\2024-10-25.Team.H.@.Team.G.-.Tracking.csv", dtype={'Column_9': str})