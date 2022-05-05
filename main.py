#!/usr/bin/env python

import json
import numpy as np
from scipy import stats
import os
import sys
from pathlib import Path
import h5py



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


data_file = str(config['timeseries'])


print("Loading time series...")

ts=pd.read_csv('data_file')
ts=ts['timeseries']
#hf = h5py.File(data_file,'r') #load data 
#reglabs = np.array(hf.get('regionids')).astype(np.str) #region_ids
#ts = np.array(hf.get('timeseries')) #time series


