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
outputDirectory = "output/csv"

if(not os.path.exists(outputDirectory)):
    os.makedirs(outputDirectory)


# Reading config file
with open(configFilename, "r") as fd:
    config = json.load(fd)




print("Loading time series...")

timeseriesFilename = config["tsv"]

ts = pd.read_csv(timeseriesFilename,sep="\t")

K = np.sum(ts, axis=0)
columns=ts.columns
ts=ts.drop(columns[np.where(K == 0)[0]],axis=1)



# z-scored time series
z = stats.zscore(np.asarray(ts),1)


print("Building edge time series...")
T, N= ts.shape
u,v = np.where(np.triu(np.ones(N),1))           # get edges
# element-wise prroduct of time series
ets = (z[:,u]*z[:,v])
edgeids = {"edgeid"+str(e):edge for e,edge in enumerate(zip(columns[u],columns[v]))}

np.savetxt('output/csv/edge_timeseries.csv',ets,delimiter=',') 
with open('output/edgeids.json', 'w') as outfile:
    json.dump(edgeids,outfile)