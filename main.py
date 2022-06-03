#!/usr/bin/env python

import json
import numpy as np
from scipy import stats
import os
import sys
from pathlib import Path
import pandas as pd



# Choosing config file
configFilename = "config-sample.json"
argCount = len(sys.argv)
if(argCount > 1):
    configFilename = sys.argv[1]

# Defining paths
outputDirectory = "output"

if(not os.path.exists(outputDirectory)):
    os.makedirs(outputDirectory)

# Reading config file
with open(configFilename, "r") as fd:
    config = json.load(fd)




print("Loading time series...")

timeseriesFilename = config["tsv"]

ts = pd.read_csv(timeseriesFilename,sep="\t")
columns=ts.columns
# z-scored time series
z = stats.zscore(ts,1)


print("Building edge time series...")
T, N= ts.shape
u,v = np.where(np.triu(np.ones(N),1))           # get edges
# element-wise prroduct of time series
ets = (z.iloc[:,u]*z.iloc[:,v])
edgeids = [edge for edge in zip(columns[u],columns[v])]

np.savetxt('outputDirectory/edge_timeseries.csv',np.asarray(ets),delimiter=',') 
np.savetxt('outputDirectory/edge_ids.csv',np.array(edgeids),delimiter=',') 