#!/usr/bin/env python

import json
import numpy as np
from scipy import stats
import os
import sys
from pathlib import Path
import pandas as pd
import csv



# Choosing config file
configFilename = "config.json"
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
z = stats.zscore(np.asarray(ts),1)


print("Building edge time series...")
T, N= ts.shape
u,v = np.where(np.triu(np.ones(N),1))           # get edges
# element-wise prroduct of time series
ets = (z[:,u]*z[:,v])
edgeids = {"edgeid"+str(e):edge for e,edge in enumerate(zip(columns[u],columns[v]))}




ets_pd = pd.DataFrame(ets, columns=[e for e,edge in enumerate(zip(columns[u],columns[v]))])
ets_pd.to_csv('output/timeseries.tsv',sep='\t', index=False)

with open('output/timeseries.json', 'w') as outfile:
     outfile.write(json.dumps(edgeids))

