import h5py
import numpy as np
import time
import os
import glob

# Convert the hdf5 file from metavision format to only events format 
def convertedHDF5(original_path):
    start_time = time.time()

    with h5py.File(original_path, "r") as f:
        final_path = '/media/exx/Elements/aayush/rvt/dataset/h5_files/new_' + original_path.split('/')[-1]

        final = h5py.File(final_path, "w")
        evts = f["CD"]
        group = final.create_group("events")

        print(evts['events']['x'].size)
        xdataset = group.create_dataset('x', data = evts['events']['x'], chunks=True, compression="gzip",) 
        ydataset = group.create_dataset('y', data = evts['events']['y'], chunks=True, compression="gzip")
        pdataset = group.create_dataset('p', data = evts['events']['p'], chunks=True, compression="gzip")
        tdataset = group.create_dataset('t', data = evts['events']['t'], chunks=True, compression="gzip")
        hdataset = group.create_dataset('height', data = 720)
        wdataset = group.create_dataset('width', data = 1280)

        final.close()

    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")


if __name__ == "__main__":

    original_folder = '/media/exx/Elements/aayush/data/h5data/tmpfodler'
    h5_files = glob.glob(os.path.join(original_folder, '*.hdf5'))

    for original_path in h5_files:
        convertedHDF5(original_path)

