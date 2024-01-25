import numpy as np
import os
import glob

NUM_CLASSES = 8
FIND_ASPECT_RATIO = True

def findAreaOfBBox(area_array, boxes):
    pass

    for box in boxes:
        area = box['w']*box['h']
        # if area < 45_000: # approx 5%
        if area <= 1024: # COCO format
            area_array[box['class_id']][0] += 1
            area_array[NUM_CLASSES][0] += 1

        # elif area < 140_000: # approx 15%
        elif area <= 9216: # COCO format
            area_array[box['class_id']][1] += 1
            area_array[NUM_CLASSES][1] += 1

        else:
            area_array[box['class_id']][2] += 1
            area_array[NUM_CLASSES][2] += 1


if __name__ == "__main__":
    path = ''
    files = glob.glob(os.path.join(path, '**/*.npy'), recursive=True)    
    
    area_array = [[0 for _ in range(3)] for _ in range(NUM_CLASSES+1)]

    for file in files:
        boxes = np.load(file)
        findAreaOfBBox(area_array, boxes)

    print(area_array)