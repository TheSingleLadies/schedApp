NUM_PATIENTS = 0
NUM_CARE_TEAMS = 0
NUM_SLOTS = 96

PatientArray = np.zeros((NUM_PATIENTS, NUM_SLOTS))
CareTeamArray = np.zeros((NUM_CARE_TEAMS, NUM_SLOTS))



import numpy as np

class WorkOrder:
    """ represents a work order """
    expectedStart = 0
    expectedEnd = 0
    
    def __init__(self, startTime, endTime, length, patient, careTeam, prereqs):
        self.startTime = startTime
        self.endTime = endTime
        self.expectedStart = startTime
        self.expectedEnd = endTime
        self.length = length
        self.patient = patient
        self.careTeam = careTeam
        self.prereqs = prereqs

    def flexTime(self):
        return self.expectedStart - self.expectedEnd - self.length


def main():
    

    
    
        
