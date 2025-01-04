import pandas as pd
import seaborn as sn
import hockey_rink as hockey_rink
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from sportypy.surfaces.hockey import NHLRink
ba_tracking = pd.read_csv(r"data\2024-10-13.Team.B.@.Team.A.-.Tracking.csv")
ba_tracking.replace({'n/a': '', 'Go': ''}, inplace=True)
ba_tracking.to_csv(r"data\new_2024-10-13.Team.B.@.Team.A.-.Tracking.csv", index = False)

dc_tracking = pd.read_csv(r"data\2024-11-15.Team.D.@.Team.C.-.Tracking.csv")
dc_tracking.replace({'n/a': '', 'Go': ''}, inplace=True)
dc_tracking.to_csv(r"data\new_2024-11-15.Team.D.@.Team.C.-.Tracking.csv", index = False)


fe_tracking = pd.read_csv(r"data\2024-11-16.Team.F.@.Team.E.-.Tracking.csv")
fe_tracking.replace({'n/a': '', 'Go': ''}, inplace=True)
fe_tracking.to_csv(r"data\new_2024-11-16.Team.F.@.Team.E.-.Tracking.csv", index = False)
