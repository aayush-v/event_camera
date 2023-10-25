"""
Script to upsize the bounding boxes location and size by a FACTOR (due to downsizing videos for labeling)
"""
import numpy as np

FACTOR_Y = 1.5
FACTOR_X = 1.77

def upsizeBoundingBoxSize(path):
    arr = np.load(path)

    arr['x'] = arr['x']*FACTOR_X
    arr['y'] = arr['y']*FACTOR_Y

    arr['h'] = arr['h']*FACTOR_Y
    arr['w'] = arr['w']*FACTOR_X

    np.save('/home/exx/Documents/aayush/currentData/test_data/test_data_updated_bbox.npy', arr)


if __name__ == "__main__":
    # npy_file = "/media/exx/Elements/aayush/1MPX_data/test/17-04-04_11-00-13_cut_15_183500000_243500000_bbox.npy"
    # npy_file = "/media/exx/E4D8-27DA/Event_data/july27_working_dir/raw_data/labels_output/nighttime/19-50-15_bbox.npy"
    # npy_file = "/media/exx/Elements/aayush/data/event_data/annotations/npy_files/09-19-01_bbox.npy"
    npy_file = "/home/exx/Documents/aayush/currentData/test_data/test_data_bbox.npy"

    upsizeBoundingBoxSize(npy_file)

