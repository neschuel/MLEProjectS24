# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 23:44:43 2024

@author: Nick

https://www.nist.gov/el/intelligent-systems-division-73500/degradation-measurement-robot-arm-position-accuracy
"""
#inputs: target position, velocity, accleration
#       payload
#outputs: positional error


import pandas as pd
import numpy as np
fullfn = "data/robotArmData.csv"
prunedfn = "data/prunedArmData.csv"
payloadfn = "data/payloads.csv"
targposfn = "data/targetpositions.csv"
targvelfn = "data/targetvelocities.csv"
targaccfn = "data/targetaccelerations.csv"
targcurfn = "data/targetcurrents.csv"
errposfn = "data/errorpositions.csv"
fulldf = pd.read_csv(fullfn) #read into pandas data frame
# print(fulldf)


#dftime = fulldf[fulldf.columns[[0]]]
dfjtargetpositions = fulldf.iloc[:,1:7]
dfjactualpositions = fulldf.iloc[:,7:13]
dfjtargetvelocities = fulldf.iloc[:,13:19]
#dfjactualvelocities = fulldf.iloc[:,19:25]
dfjtargetcurrents = fulldf.iloc[:,25:31]
#dfjactualcurrents = fulldf.iloc[:,31:37]
dfjtargetaccelerations = fulldf.iloc[:,37:43]
dfpayloads = fulldf.iloc[:,75]

jerrorpositions = dfjactualpositions.to_numpy() - dfjtargetpositions.to_numpy()
dfjerrorpositions = pd.DataFrame(jerrorpositions)
# print(dfjactualpositions)
# print(dfjtargetpositions)
# print(dfjerrorpositions)

pruneddf = pd.concat([dfpayloads,
                      dfjtargetpositions,
                      dfjtargetvelocities,
                      dfjtargetaccelerations,
                      dfjtargetcurrents,
                      dfjerrorpositions],axis = 1)

# print(pruneddf)
pruneddf.to_csv(prunedfn, header=False, index=False)
dfpayloads.to_csv(payloadfn,header=False,index=False)
dfjtargetpositions.to_csv(targposfn,header=False,index=False)
dfjtargetvelocities.to_csv(targvelfn,header=False,index=False)
dfjtargetaccelerations.to_csv(targaccfn,header=False,index=False)
dfjtargetcurrents.to_csv(targcurfn,header=False,index=False)
dfjerrorpositions.to_csv(errposfn,header=False,index=False)

# cutdf = fulldf.drop(fulldf.columns[[43,44,45,46,47,48, #drop torques
#                                     49,50,51,52,53,54, #drop control current
#                                     55,56,57,58,59,60, #drop cartesian coords
#                                     61,62,63,64,65,66, #drop force
#                                     67,68,69,70,71,72, #drop temperature
#                                     73,74,76]], #drop start, speed, test num, keep payload
#                                     axis=1)
#remaining: time = 0
#        payload = 43
#