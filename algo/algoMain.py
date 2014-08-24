#Google Api Auth Imports
from apiclient.discovery import build
from oauth2client.client import OAuth2WebServerFlow
import httplib2

#Calendar API Imports
import gflags
import httplib2
from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run

NUM_PATIENTS = 0
NUM_CARE_TEAMS = 0
NUM_SLOTS = 96
INTERVAL_MINUTES = 15
INTERVAL_MS = INTERVAL_MINUTES*60*1000

PatientArray = np.zeros((NUM_PATIENTS, NUM_SLOTS))
CareTeamArray = np.zeros((NUM_CARE_TEAMS, NUM_SLOTS))
FlexTimes = {}

AllOrders = []
service = ""
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

def initGoogleCalendarApi():
    FLAGS = gflags.FLAGS
    # Set up a Flow object to be used if we need to authenticate. 
    FLOW = OAuth2WebServerFlow(
        client_id='219950026323-beqmmmrta5ufs6au8lfdm60gq3no8393.apps.googleusercontent.com',
        client_secret='DKWe_J5lGANQopyLI4H-2DCa',
        scope='https://www.googleapis.com/auth/calendar',
        user_agent='SchedApp/1.0')
    # If the Credentials don't exist or are invalid, run through the native client
    # flow. The Storage object will ensure that if successful the good
    # Credentials will get written back to a file.
    storage = Storage('calendar.dat')
    credentials = storage.get()
    if credentials is None or credentials.invalid == True:
      credentials = run(FLOW, storage)

    # Create an httplib2.Http object to handle our HTTP requests and authorize it
    # with our good Credentials.
    http = httplib2.Http()
    http = credentials.authorize(http)

    # Build a service object for interacting with the API. Visit
    # the Google Developers Console
    # to get a developerKey for your own application.
    service = build(serviceaNme='calendar', version='v3', http=http,
           developerKey='AIzaSyDAaAfE6Zjs8OMmfj3SB5O3r_2sf1CPeWU')

        
##def algo():
##    for workOrder in AllOrders:
##        for i in range(workOrder.expectedStart, workOrder.expectedEnd+1, INTERVAL_MINUTES)
##            if not PatientArray[pNum][i] == 0 or not PatientArray[ctNum][i] == 0:
##                flag = true
##                break

def main():
    initGoogleCalendarApi()
    calendar = service.calendars().get(calendarId='primary').execute()
    id = calendar['id']
    print id
                
