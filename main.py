import json
import numpy as np
from scipy import stats
import h5py



# load inputs from config.json
with open('config-sample.json') as config_json:
    config = json.load(config_json)
    
data_file = str(config['time_series'])



hf = h5py.File(data_file,'r') #load data 
reglabs = np.array(hf.get('regionids')).astype(np.str) #region_ids
ts = np.array(hf.get('timeseries')) #time series

# z-scored time series
z = stats.zscore(ts,0)
        
T,N= ts.shape
u,v = np.where(np.triu(np.ones(N),1))           # get edges
# element-wise prroduct of time series
ets = z[:,u]*z[:,v]                           

hf.close()                            
np.savetxt('outputDirectory/edge_timeseries.csv',ets.transpose(),delimiter=',') 