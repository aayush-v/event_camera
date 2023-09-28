import numpy as np


def convert_npy(npy_file):
    old_npy = np.load(npy_file)

    converted_dtype = [('t', '<u8'), ('x', '<f4'), ('y', '<f4'), ('w', '<f4'), ('h', '<f4'), ('class_id', 'u1'), ('class_confidence', '<f4'), ('track_id', '<u4')]

    converted_npy = np.empty(old_npy.shape, dtype=converted_dtype)

    converted_npy['t'] = old_npy['t']
    converted_npy['x'] = old_npy['x']
    converted_npy['y'] = old_npy['y']
    converted_npy['w'] = old_npy['w']
    converted_npy['h'] = old_npy['h']
    converted_npy['class_id'] = old_npy['class_id']
    converted_npy['class_confidence'] = old_npy['class_confidence']
    converted_npy['track_id'] = old_npy['track_id']
    print("NPY format updated")
    np.save('new_npy.npy', converted_npy)

if __name__ == "__main__":
    # npy_file = "/media/exx/Elements/aayush/1MPX_data/test/17-04-04_11-00-13_cut_15_183500000_243500000_bbox.npy"
    npy_file = "/media/exx/E4D8-27DA/Event_data/july27_working_dir/raw_data/labels_output/nighttime/19-50-15_bbox.npy"
    convert_npy(npy_file)

