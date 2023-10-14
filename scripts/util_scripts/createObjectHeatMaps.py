import numpy as np
import matplotlib.pyplot as plt
import os
import glob

NUM_CLASSES = 8
IMAGE_HEIGHT = 720
IMAGE_WIDTH = 1024

def updateHeatMaps(heatmap, boxes):
    for box in boxes:
        heatmap[box['class_id']][int(box['y']):int(box['y'] + box['h']), 
                int(box['x']): int(box['x'] + box['w'])] += 1


if __name__ == "__main__":
    path = '/Users/aayushverma/Downloads/final_annotations'
    files = glob.glob(os.path.join(path, '*.npy'))

    heatmap = np.zeros((NUM_CLASSES, IMAGE_HEIGHT, IMAGE_WIDTH))

    for file in files:
        boxes = np.load(file)

        updateHeatMaps(heatmap, boxes)

    for idx in range(NUM_CLASSES):
        class_heatmap = heatmap[idx, :, :]
        class_heatmap = class_heatmap / np.max(class_heatmap)

        plt.subplot(2,4, idx+1)

        plt.imshow(class_heatmap, cmap='hot')
        plt.title(f'Class {idx+1}')

    plt.tight_layout()
    plt.show()