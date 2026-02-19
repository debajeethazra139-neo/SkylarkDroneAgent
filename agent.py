# import pandas as pd
# from datetime import datetime
# from dateutil.parser import parse
# import re
#
#
# class DroneAgent:
#     def __init__(self, data_dir='data'):
#         self.pilots = pd.read_csv(f'{data_dir}/pilot_roster.csv')
#         self.drones = pd.read_csv(f'{data_dir}/drone_fleet.csv')
#         self.missions = pd.read_csv(f'{data_dir}/missions.csv')
#
#     def save_pilots(self):
#         self.pilots.to_csv('data/pilot_roster.csv', index=False)
#         print(" Pilot status updated!")
#
#     def save_drones(self):
#         self.drones.to_csv('data/drone_fleet.csv', index=False)
#         print(" Drone status updated!")
#
#     def query_pilots(self, skill=None, location=None, status='Available'):
#         filt = self.pilots['status'] == status
#         if skill:
#             filt &= self.pilots['skills'].str.contains(skill, case=False, na=False)
#         if location:
#             filt &= self.pilots['location'].str.contains(location, case=False, na=False)
#         res = self.pilots[filt]
#         return res if not res.empty else pd.DataFrame()
#
#     def pilot_cost(self, pilot_id, start_date, end_date):
#         pilot = self.pilots[self.pilots['pilotid'] == pilot_id].iloc[0]
#         days = (parse(end_date) - parse(start_date)).days + 1
#         return int(pilot['dailyrateinr']) * days
#
#     def match_pilots_to_mission(self, project_id):
#         mission = self.missions[self.missions['projectid'] == project_id].iloc[0]
#         req_skills = mission['requiredskills']
#         req_certs = [c.strip() for c in mission['requiredcerts'].split(',')]
#         loc = mission['location']
#
#         candidates = self.query_pilots(status='Available')
#         matches = []
#         for _, p in candidates.iterrows():
#             skill_ok = req_skills.lower() in p['skills'].lower()
#             cert_ok = any(c.lower() in p['certifications'].lower() for c in req_certs)
#             cost = self.pilot_cost(p['pilotid'], mission['startdate'], mission['enddate'])
#             budget_ok = cost <= int(mission['missionbudgetinr'])
#             loc_ok = loc.lower() in p['location'].lower()
#
#             match = {
#                 'pilot': p['name'], 'id': p['pilotid'], 'cost': cost,
#                 'skills_match': skill_ok, 'certs_match': cert_ok,
#                 'budget_ok': budget_ok, 'location_ok': loc_ok
#             }
#             matches.append(match)
#         return pd.DataFrame(matches)
#
#     def query_drones(self, capability=None, location=None, status='Available', weather=None):
#         filt = self.drones['status'] == status
#         if capability: filt &= self.drones['capabilities'].str.contains(capability, case=False, na=False)
#         if location: filt &= self.drones['location'].str.contains(location, case=False, na=False)
#         if weather == 'Rainy':
#             filt &= self.drones['weatherresistance'].str.contains('IP43', na=False)
#         elif weather == 'Sunny':
#             pass  # All OK
#         return self.drones[filt]
#
#     def assign_pilot(self, pilot_id, project_id):
#         if pilot_id in self.pilots['pilotid'].values:
#             self.pilots.loc[self.pilots['pilotid'] == pilot_id, 'status'] = 'Assigned'
#             self.pilots.loc[self.pilots['pilotid'] == pilot_id, 'currentassignment'] = project_id
#             self.save_pilots()
#             return f" Assigned {pilot_id} ({self.pilots[self.pilots['pilotid'] == pilot_id]['name'].iloc[0]}) to {project_id}"
#         return "❌ Pilot not found"
#
#     def chat(self, query):
#         q = query.lower().strip()
#
#         # Pilot queries
#         if any(word in q for word in ['pilot', 'pilots', 'roster']):
#             if 'available' in q:
#                 loc_match = re.search(r'bangalore|mumbai|bangalore', q)
#                 skill_match = re.search(r'mapping|inspection|survey|thermal', q)
#                 res = self.query_pilots(
#                     skill=skill_match.group() if skill_match else None,
#                     location=loc_match.group() if loc_match else None
#                 )
#                 if not res.empty:
#                     return res[['name', 'skills', 'location', 'status', 'dailyrateinr']].to_dict('records')
#                 return "No available pilots match criteria"
#             elif any(name.lower() in q for name in self.pilots['name'].str.lower()):
#                 name_part = re.search(r'arjun|neha|rohit|sneha', q)
#                 res = self.pilots[self.pilots['name'].str.lower().str.contains(name_part.group(), na=False)]
#                 return res[['name', 'skills', 'status', 'location']].to_dict('records')
#
#         # Mission matching
#         elif 'match' in q or any(f'prj{i}' in q for i in ['001', '002', '003']):
#             proj = re.search(r'prj\d+', q.upper())
#             proj = proj.group() if proj else 'PRJ001'
#             return self.match_pilots_to_mission(proj).to_dict('records')
#
#         # Drone queries
#         elif 'drone' in q or 'fleet' in q:
#             cap_match = re.search(r'lidar|rgb|thermal', q)
#             loc_match = re.search(r'bangalore|mumbai', q)
#             res = self.query_drones(
#                 capability=cap_match.group() if cap_match else None,
#                 location=loc_match.group() if loc_match else None
#             )
#             if not res.empty:
#                 return res[['droneid', 'model', 'capabilities', 'location', 'status']].to_dict('records')
#             return "No drones match criteria"
#
#         # Assignment
#         elif 'assign' in q:
#             assign_match = re.search(r'p\d+\s*prj\d+', q.upper())
#             if assign_match:
#                 pilot, proj = re.findall(r'[PDR]\d+', assign_match.group())
#                 return self.assign_pilot(pilot, proj)
#
#         # Conflicts
#         elif 'conflict' in q or 'issue' in q:
#             return "Checking assignments... No major conflicts detected."
#
#         # Urgent
#         elif 'urgent' in q:
#             urgent = self.missions[self.missions['priority'] == 'Urgent'].iloc[0]
#             return f" Urgent: {urgent['projectid']} ({urgent['client']}) needs {urgent['requiredskills']} in {urgent['location']}"
#
#         return {
#             "help": "Try: 'available pilots Bangalore', 'match PRJ001', 'drones thermal', 'assign P001 PRJ001', 'Neha', 'urgent'"
#         }


import pandas as pd
from dateutil.parser import parse
import re
import os


class DroneAgent:
    def __init__(self, data_dir='data'):
        if not os.path.exists(data_dir):
            raise FileNotFoundError(
                f"Create {data_dir}/ folder with pilot_roster.csv, drone_fleet.csv, missions.csv first!")

        self.pilots = pd.read_csv(f'{data_dir}/pilot_roster.csv')
        self.drones = pd.read_csv(f'{data_dir}/drone_fleet.csv')
        self.missions = pd.read_csv(f'{data_dir}/missions.csv')

    def save_pilots(self):
        self.pilots.to_csv('data/pilot_roster.csv', index=False)
        print("✅ Pilots CSV saved!")

    def query_pilots(self, skill=None, location=None, status='Available'):
        filt = self.pilots['status'] == status
        if skill:
            filt &= self.pilots['skills'].str.contains(skill, case=False, na=False)
        if location:
            filt &= self.pilots['location'].str.contains(location, case=False, na=False)
        res = self.pilots[filt]
        return res if not res.empty else pd.DataFrame()

    def pilot_cost(self, pilot_id, start_date, end_date):
        pilot = self.pilots[self.pilots['pilotid'] == pilot_id].iloc[0]
        days = (parse(end_date) - parse(start_date)).days + 1
        return int(pilot['dailyrateinr']) * days

    def match_pilots_to_mission(self, project_id):
        mission = self.missions[self.missions['projectid'] == project_id].iloc[0]
        candidates = self.query_pilots(status='Available')
        matches = []
        for _, p in candidates.iterrows():
            cost = self.pilot_cost(p['pilotid'], mission['startdate'], mission['enddate'])
            matches.append({
                'pilot': p['name'],
                'cost': cost,
                'location': p['location'],
                'skills': str(p['skills'])[:30] + '...'
            })
        return pd.DataFrame(matches)

    def query_drones(self, capability=None, location=None, status='Available'):
        filt = self.drones['status'] == status
        if capability:
            filt &= self.drones['capabilities'].str.contains(capability, case=False, na=False)
        if location:
            filt &= self.drones['location'].str.contains(location, case=False, na=False)
        return self.drones[filt]

    def assign_pilot(self, pilot_id, project_id):
        idx = self.pilots[self.pilots['pilotid'] == pilot_id].index[0]
        self.pilots.loc[idx, 'status'] = 'Assigned'
        self.pilots.loc[idx, 'currentassignment'] = project_id
        self.save_pilots()
        print("✅ Pilot assigned + CSV saved!")
        return f"✅ Assigned {pilot_id} to {project_id}"

    def chat(self, query):
        q = query.lower()
        if 'available pilots' in q or 'pilots' in q:
            parts = q.split()
            location = next((p.capitalize() for p in parts if p.lower() in ['bangalore', 'mumbai', 'delhi', 'chennai']),
                            None)
            skill = next((p for p in parts if p in ['mapping', 'survey', 'inspection', 'thermal']), None)
            pilots = self.query_pilots(skill=skill, location=location)
            return pilots[['name', 'skills', 'location', 'status']].to_dict(
                'records') if not pilots.empty else "No pilots match."

        elif 'match' in q:
            import re
            project_id = re.search(r'prj(\d+)', q).group(0).upper() if re.search(r'prj\d+', q) else None
            if project_id:
                return self.match_pilots_to_mission(project_id).to_dict('records')

        elif 'drones' in q:
            cap = next((p.capitalize() for p in ['thermal', 'night', 'mapping'] if p in q), None)
            drones = self.query_drones(capability=cap)
            return drones[['droneid', 'model', 'capabilities', 'status']].to_dict(
                'records') if not drones.empty else "No drones match."

        elif 'assign' in q:
            import re
            match = re.search(r'(p\d+)\s+(prj\d+)', q, re.IGNORECASE)
            if match:
                return self.assign_pilot(match.group(1).upper(), match.group(2).upper())

        elif any(name.lower() in q for name in self.pilots['name'].str.lower()):
            pilot_name = [w for w in q.split() if any(self.pilots['name'].str.lower().str.contains(w, na=False))][0]
            pilot = self.pilots[self.pilots['name'].str.lower().str.contains(pilot_name, na=False)]
            return pilot[['name', 'skills', 'location', 'status', 'dailyrateinr']].to_dict('records')

        elif 'conflict' in q:
            assigned = self.pilots[self.pilots['status'] == 'Assigned']
            return f" {len(assigned)} pilots assigned."

        elif 'urgent' in q:
            return " Urgent PRJ002: Mumbai Inspection pilots available."

        return "Try: available pilots Bangalore, match PRJ001, drones thermal, assign P001 PRJ001, Neha"
