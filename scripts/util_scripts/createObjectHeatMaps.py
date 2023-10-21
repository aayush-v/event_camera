import numpy as np
import matplotlib.pyplot as plt
import os
import glob
from objects import eTraP_CLASS_TO_IDX_MAPPING, value_to_key
import seaborn as sns
 
NUM_CLASSES = 8
IMAGE_HEIGHT = 720
IMAGE_WIDTH = 1024

def updateHeatMaps(heatmap, boxes):
    for box in boxes:
        heatmap[box['class_id']][int(box['y']):int(box['y'] + box['h']), 
                int(box['x']): int(box['x'] + box['w'])] += 1


if __name__ == "__main__":
    # path = '/media/exx/data/aayush/dataset/analysis/annots/daytime_intersection'
    # files = glob.glob(os.path.join(path, '*.npy'))

    path = '/media/exx/data/aayush/dataset/final_annotations'
    files = glob.glob(os.path.join(path, '**/*.npy'), recursive=True)

    heatmap = np.zeros((NUM_CLASSES, IMAGE_HEIGHT, IMAGE_WIDTH))

    for file in files:
        boxes = np.load(file)

        updateHeatMaps(heatmap, boxes)

    for idx in range(NUM_CLASSES):
        class_heatmap = heatmap[idx, :, :]
        class_heatmap = class_heatmap / np.max(class_heatmap)
        print('creating heatmap...')
        sns.heatmap(class_heatmap, cmap="crest")

        # plt.xlabel('')

        plt.subplot(2,4, idx+1)

        plt.imshow(class_heatmap, cmap='cool')
        plt.title(f'Class {value_to_key(eTraP_CLASS_TO_IDX_MAPPING, idx)}')
        plt.axis('off')

        # plt.show()


    plt.tight_layout()
    plt.show()