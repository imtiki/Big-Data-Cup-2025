import pandas as pd
from Import import dc_tracking, dc_shifts, dc_events, fe_shifts, fe_events, hg_shifts, hg_events, fe_tracking, hg_tracking

def to_seconds(x):
    colo = x.find(":")
    mins_str = x[0:colo]
    mins = int(mins_str)
    sec_str = x[colo+1:]
    secs = int(sec_str)
    return (mins * 60) + secs


dc_shifts['start_clock'] = dc_shifts['start_clock'].apply(to_seconds)
dc_shifts['end_clock'] = dc_shifts['end_clock'].apply(to_seconds)
dc_shifts['shift_length'] = dc_shifts['shift_length'].apply(to_seconds)
dc_events['Clock'] = dc_events['Clock'].apply(to_seconds)
dc_tracking['Game Clock'] = dc_tracking['Game Clock'].apply(to_seconds)

fe_shifts['start_clock'] = fe_shifts['start_clock'].apply(to_seconds)
fe_shifts['end_clock'] = fe_shifts['end_clock'].apply(to_seconds)
fe_shifts['shift_length'] = fe_shifts['shift_length'].apply(to_seconds)
fe_events['Clock'] = fe_events['Clock'].apply(to_seconds)
fe_tracking['Game Clock'] = fe_tracking['Game Clock'].apply(to_seconds)

hg_shifts['start_clock'] = hg_shifts['start_clock'].apply(to_seconds)
hg_shifts['end_clock'] = hg_shifts['end_clock'].apply(to_seconds)
hg_shifts['shift_length'] = hg_shifts['shift_length'].apply(to_seconds)
hg_events['Clock'] = hg_events['Clock'].apply(to_seconds)
#hg_tracking['Game Clock'] = hg_tracking['Game Clock'].apply(to_seconds)

fe_shifts = fe_shifts[fe_shifts['Player_Id'] != 'Go']
dc_shifts = dc_shifts[dc_shifts['Player_Id'] != 'Go']
hg_shifts = hg_shifts[hg_shifts['Player_Id'] != 'Go']
fe_events = fe_events[fe_events['Player_Id'] != 'Go']
dc_events = dc_events[dc_events['Player_Id'] != 'Go']
dc_events = dc_events[dc_events['Player_Id'] != 'Go']
