# Save as setup_data.py and run: python setup_data.py
import pandas as pd
import os
os.makedirs('data', exist_ok=True)

pilots_data = {
    'pilotid': ['P001', 'P002', 'P003', 'P004'],
    'name': ['Arjun', 'Neha', 'Rohit', 'Sneha'],
    'skills': ['Mapping, Survey', 'Inspection', 'Inspection, Mapping', 'Survey, Thermal'],
    'location': ['Bangalore', 'Mumbai', 'Mumbai', 'Bangalore'],
    'status': ['Available', 'Available', 'Available', 'Available'],
    'dailyrateinr': [1500, 1800, 1600, 1700],
    'currentassignment': ['', '', '', '']
}
pd.DataFrame(pilots_data).to_csv('data/pilot_roster.csv', index=False)

drones_data = {
    'droneid': ['D001', 'D002', 'D003', 'D004'],
    'model': ['DJI Phantom 4', 'DJI Mavic 2', 'DJI Mavic 3T', 'DJI Matrice 30'],
    'capabilities': ['Mapping', 'Survey', 'Thermal, Night', 'Thermal, Mapping'],
    'location': ['Bangalore', 'Mumbai', 'Bangalore', 'Mumbai'],
    'status': ['Available', 'Available', 'Available', 'Maintenance']
}
pd.DataFrame(drones_data).to_csv('data/drone_fleet.csv', index=False)

missions_data = {
    'projectid': ['PRJ001', 'PRJ002', 'PRJ003'],
    'client': ['Client A', 'Client B', 'Client C'],
    'requiredskills': ['Mapping', 'Inspection', 'Thermal'],
    'location': ['Bangalore', 'Mumbai', 'Bangalore'],
    'startdate': ['2026-02-20', '2026-02-25', '2026-03-01'],
    'enddate': ['2026-02-22', '2026-03-01', '2026-03-05']
}
pd.DataFrame(missions_data).to_csv('data/missions.csv', index=False)

print(" Data ready!")
