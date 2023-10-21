import numpy as np
import matplotlib.pyplot as plt
import os
import glob
from objects import eTraP_CLASS_TO_IDX_MAPPING, value_to_key
from matplotlib.font_manager import FontProperties
import math

NUM_CLASSES = 8
FIND_ASPECT_RATIO = True

def aspectRatioFrequency(aspect_ratios, boxes):
    pass

    for box in boxes:
        aspect_ratios[box['class_id']].append(box['w']/box['h'])




if __name__ == "__main__":
    path = '/media/exx/data/aayush/dataset/analysis/annots/daytime_intersection'
    path = '/media/exx/data/aayush/dataset/final_annotations'
    files = glob.glob(os.path.join(path, '**/*.npy'), recursive=True)



    aspect_ratios = []
    for i in range(NUM_CLASSES):
        aspect_ratios.append([])

    print(aspect_ratios)
    for file in files:
        boxes = np.load(file)
        aspectRatioFrequency(aspect_ratios, boxes)

    # fig, axes = plt.subplots(2, 4, figsize=(15, 10))
    # axes.flatten()

    for idx in range(NUM_CLASSES):
        class_aspect_ratio = aspect_ratios[idx]
        class_aspect_ratio = [x for x in class_aspect_ratio if x <= 6]
        
        # ax = axes[idx // 4, idx % 4]
        print(len(class_aspect_ratio))
        # plt.hist(class_aspect_ratio, bins = max(50, int(len(class_aspect_ratio) ** (1./3))), edgecolor='skyblue')
        # bins=int(math.sqrt(len(class_aspect_ratio))/2)
        plt.xlim(0,6)
        # ax.set_title(f'Class {value_to_key(eTraP_CLASS_TO_IDX_MAPPING, idx)}')

        plt.tight_layout()
        plt.rcParams['font.family'] = 'Times'
        plt.rcParams['font.size'] = 12
        plt.show()
