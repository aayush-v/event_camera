import h5py
import numpy as np
import time

# Convert the hdf5 file from metavision format to only events format 
start_time = time.time()

original_file_path = '/media/exx/Elements/aayush/rvt/test1/h5exp/singleHandWaving_New_activity.hdf5'
final_path = 'new_file.hdf5'

with h5py.File(original_file_path, "r") as f:
    final = h5py.File(final_path, "w")
    chunk_shape = (16384,)
    evts = f["CD"]
    group = final.create_group("events")


    print(evts['events']['x'].size)
    xdataset = group.create_dataset('x', data = evts['events']['x'], chunks=True, compression="gzip",) 
    ydataset = group.create_dataset('y', data = evts['events']['y'], chunks=True, compression="gzip")
    pdataset = group.create_dataset('p', data = evts['events']['p'], chunks=True, compression="gzip")
    tdataset = group.create_dataset('t', data = evts['events']['t'], chunks=True, compression="gzip")
    dividerdataset = group.create_dataset('divider', data = 1)
    hdataset = group.create_dataset('height', data = 1280)
    wdataset = group.create_dataset('width', data = 720)

    final.close()

end_time = time.time()


elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.2f} seconds")



