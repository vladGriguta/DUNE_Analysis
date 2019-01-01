#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 20:41:11 2018

@author: vladgriguta
"""


# This is the high level coding structure where all functions
# are called

import numpy as np
import pandas as pd
import genericFunctions
import readFiles



# Define constant parameters in the simulation
simulationTime = float(input('Please imput the simulation duration (in seconds):\n'))
resolution = float(input('Please imput the resolution expected (in microseconds):\n'))
#trigDur = float(input('Please give the dead time of the trigger (we ended up using 0):\n'))
trigDur = 0
version = input('Please input a distinctive code for current analysis (e.g. date):\n')

# Call functions to read from files
location = '../finalCSVfiles/'
print('Reading data from files... Simulation time = '+str(simulationTime/1000000)+' seconds')
timeSN,nr_events_SN = readFiles.Read_SN(location)
timeAr,nr_events_Ar = readFiles.Read_Ar39(location)
print('Finished reading from files.')

# Compute the noise (mean number of photons from Ar39 per microseconds)
noise = float(len(timeAr))/simulationTime

print('The mean number of Ar39 events per microsecond is '+str(nr_events_Ar/simulationTime)
      +'. Compare with expected number of (about) 0.8 photons per microsecond.')
print('The mean number of Ar39 photons per microsecond is '+str(len(timeAr)/simulationTime)
      +'. Compare with expected number of (about) 1.8 photons per microsecond.')


events, time_and_PD = genericFunctions.DivideDataByRes(timeSN,timeAr,simulationTime,resolution=resolution)

# For now, all events are generated in the centre of each time_frame (2.5 ms).
# Therefore, the time of each SN event can be easily computed, as follows
eventsSN = pd.DataFrame()
eventsSN['eventTime'] = np.linspace(0,int(simulationTime/2500)-1,int(simulationTime/2500))*(2500)+1250
eventsSN['event'] = np.linspace(0,int(simulationTime/2500)-1,int(simulationTime/2500))

# Delete unnecesary data 
import gc
del timeSN, timeAr
gc.collect()

"""
SNCandidates, fakeTrig, SNTrig = genericFunctions.Candidates(events=events, threshold=18,
                                            integTime=2.5, eventsSN=eventsSN, trigDur=2.5,
                                            resolution=resolution,noise=noise, threshold2=threshold2,
                                            time_and_PD=time_and_PD)
"""

# This is where you can insert the datapoints over which the grid search is run
thresholdVals = [10,20,30,40,50]
integTimeVals = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8]
threshold2Vals = [[0,0],[5,2],[3,4],[4,4],[3,5],[4,5],[3,6]]


# Create an instance of the Grid search class which saves all relevant attributes
# for the analysis

GS = genericFunctions.GridSearch(thresholdVals, integTimeVals, threshold2Vals,events,
                                 eventsSN, trigDur,resolution,version,time_and_PD,simulationTime)

results = GS.ActualGridSearch()

print('The results of the full simulation are:\n'+str(results))


locationResults = '../analysisResults'
with open(locationResults+'efficiencyandFakeTrig'+str(version)+'.csv', 'w') as f:
    for item in results:
        f.write("%s\n" % str(item))
        


