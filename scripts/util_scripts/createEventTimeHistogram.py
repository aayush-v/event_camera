import h5py
import numpy as np
import time
import os
import glob
import matplotlib.pyplot as plt

HDF5_FILEPATHS = ['/Users/aayushverma/Downloads/new_10-47-27_s2_td.hdf5',
                  '/Users/aayushverma/Downloads/moorea_2019-06-26_test_02_000_976500000_1036500000_td.hdf5']

def createEventTimeHistogram(original_paths):
    f1 = h5py.File(original_paths[0], "r")
    f2 = h5py.File(original_paths[1], "r")

    num_bins = 500
    units = 1_000_00
    max_duration = min(f1['events']['t'][-1], f2['events']['t'][-1])

    bin_edges = np.linspace(1, max_duration, num_bins)
    bin_counts1, _ = np.histogram(f1['events']['t'], bins=bin_edges)
    bin_counts2, _ = np.histogram(f2['events']['t'], bins=bin_edges)

    # bin_counts1 = bin_counts1 / units
    # bin_counts2 = bin_counts2 / units

    bin_counts1 = np.log10(bin_counts1)
    bin_counts2 = np.log10(bin_counts2)

    plt.figure(figsize=(10, 6))
    print(bin_counts1.shape, bin_edges.shape, bin_counts2.shape)
    plt.plot(bin_edges[:-1], bin_counts1, label='eTraP', color='blue')
    plt.plot(bin_edges[:-1], bin_counts2, label='Gen4 automotive', color='red')
    plt.xlabel('Time')
    plt.ylabel('Frequency (per unit)')
    plt.title('Histogram of Events')
    plt.legend(loc='upper right')
    plt.show()

if __name__ == "__main__":
    createEventTimeHistogram(HDF5_FILEPATHS)
