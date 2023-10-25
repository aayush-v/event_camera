import numpy as np

def read_npy(npy_file):

    data = np.load(npy_file)
    print(f"File name: {npy_file.split('/')[-1]}")
    print(f"Shape: {data.shape}")
    print(f"DType: {data.dtype}")

    print(f"Data: {data[0:5]}")

if __name__ == "__main__":
    npy_file = "/media/exx/Elements/aayush/1MPX_data/test/17-04-04_11-00-13_cut_15_183500000_243500000_bbox.npy"
    npy_file = "/media/exx/E4D8-27DA/Event_data/july27_working_dir/raw_data/labels_output/nighttime/19-50-15_bbox.npy"
    npy_file = "/home/exx/Documents/aayush/eventSensing/new_npy.npy"
    read_npy(npy_file)
