import numpy as np
import os
import glob

def countBoundingBoxes(path):
    arr = np.load(path)

    print(f"Path {path} has: {arr.shape[0]}")
    return arr.shape[0]

   


if __name__ == "__main__":
    daytime = '/media/exx/data/aayush/dataset/final_annotations'
    nighttime = os.path.join(daytime, 'nightlabels')

    day_annotations = glob.glob(os.path.join(daytime, '*.npy'))
    night_annotations = glob.glob(os.path.join(nighttime, '*.npy'))
    
    total_daytime_bbox = 0
    total_nighttime_bbox = 0

    for npy_file in day_annotations:
        total_daytime_bbox += countBoundingBoxes(npy_file)
    for npy_file in night_annotations:
        total_nighttime_bbox += countBoundingBoxes(npy_file)

    print(f"Total bounding boxes for day time are {total_daytime_bbox}")
    print(f"Total bounding boxes for night time are {total_nighttime_bbox}")
    print(f"Total bounding boxes are {total_daytime_bbox+total_nighttime_bbox}")


