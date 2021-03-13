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

hf = h5py.File(data_file,'r') #load data 
reglabs = np.array(hf.get('regionids')).astype(np.str) #region_ids
ts = np.array(hf.get('timeseries')) #time series

# z-scored time series
z = stats.zscore(ts,0)


print("Building edge time series...")
T, N= ts.shape
u,v = np.where(np.triu(np.ones(N),1))           # get edges
# element-wise prroduct of time series
ets = (z[:,u]*z[:,v])
edgeids = [edge for edge in zip(u,v)]

hf.close()                            
# np.savetxt('outputDirectory/edge_timeseries.csv',ets.transpose(),delimiter=',') 

print("Saving hdf5 file...")
with h5py.File(Path(outputDirectory) / "timeseries.hdf5", "w")as h5f:
    h5f.create_dataset('timeseries',
                        data=ets,
                        compression="gzip")
    h5f.create_dataset('regionids',
                        data=np.array(edgeids))

# When registering the app add tag to specity this is an edge-based time series
