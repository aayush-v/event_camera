import h5py
import hdf5plugin
import numpy as np

filep = '/home/exx/Documents/aayush/eventSensing/new_file.hdf5'
# filep = '/media/exx/Elements/aayush/rvt/test1/h5exp/17-04-04_11-00-13_cut_15_61500000_121500000_td.dat.h5'
# filep = '/media/exx/Elements/aayush/rvt/test1/h5exp/singleHandWaving_New_activity.hdf5'


with h5py.File(filep, "r") as f1:
  evts = f1['events']
  print(f1)
  # print(evts['x'].size * evts['x'].itemsize) 

  for key in evts.keys():
      dataset = evts[key]
      print(f"Dataset '{key}': Shape={dataset.shape}, Dtype={dataset.dtype}, Size={dataset.size * dataset.dtype.itemsize} bytes")


#   print(evts.keys())
#   print(evts['divider'])
  print(evts['x'][:])
  
