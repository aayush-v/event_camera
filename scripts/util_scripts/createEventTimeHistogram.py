import tables
import h5py
import numpy as np
import time
import os
import glob
import matplotlib.pyplot as plt

HDF5_FILEPATHS = ['/media/exx/data/aayush/RVT/h5files/10-02-34.hdf5',
                  '/media/exx/data/aayush/1megapixel_dataset/moorea_2019-04-18_test_03_000_366500000_426500000_td.hdf5',
                  '/media/exx/data/aayush/DSEC/events.h5']

def createEventTimeHistogram(original_paths):
    f1 = h5py.File(original_paths[0], "r")
    f2 = h5py.File(original_paths[1], "r")

    f1ev = f1['events']['t'][6500000:]
    f2ev = f2['events']['t'][1500000:]

    # f3 = tables.open_file(original_paths[2], mode='r')
    # dataset = f3.root.events
    # f3ev = dataset['t']

    num_bins = 500
    units = 1_000_000
    max_duration = min(f1['events']['t'][-1], f2['events']['t'][-1])

    bin_edges = np.linspace(1, max_duration, num_bins)
    bin_counts1, _ = np.histogram(f1ev, bins=bin_edges)
    bin_counts2, _ = np.histogram(f2ev, bins=bin_edges)
    # bin_counts3, _ = np.histogram(f3ev, bins=bin_edges)

    bin_counts1 = bin_counts1 / units
    bin_counts2 = bin_counts2 / units
    # bin_counts3 = bin_counts3 / units

    plt.figure(figsize=(10, 6))
    print(bin_counts1.shape, bin_edges.shape, bin_counts2.shape)
    plt.plot(bin_edges[:-1], bin_counts1, label='eTraP', color='blue')
    plt.plot(bin_edges[:-1], bin_counts2, label='Gen4 automotive', color='red')
    # plt.plot(bin_edges[:-1], bin_counts3, label='DSEC dataset', color='green')

    plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams['font.size'] = 12
    plt.xlabel('Time')
    plt.ylabel('Frequency [MEPS]')
    plt.title('Histogram of Events')
    plt.legend(loc='upper right')
    plt.show()

if __name__ == "__main__":
    createEventTimeHistogram(HDF5_FILEPATHS)
