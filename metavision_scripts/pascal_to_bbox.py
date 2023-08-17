from bs4 import BeautifulSoup
import numpy as np
import os
from metavision_sdk_core import EventBbox
import glob

FPS = 30
FRAME_TIME = 33333
PASCAL_LABELS_DIR = '/home/exx/Documents/aayush/currentData/raw_data/july27/labels/nighttime/20-26-41/Annotations'

classes = {
    'pedestrian': 0,
    'car': 1,
    'bicycle': 2,
    'bus': 3,
    'bike': 4,
    'truck': 5,
    'tram': 6,
    'wheelchair': 7
}

########################################
with open('text_stash.txt', 'w') as txt:
    list_boxes = []

    filelist = glob.glob(os.path.join(PASCAL_LABELS_DIR, '*.xml'))
    print(len(filelist))

    for filename in sorted(filelist):
        xml_path = os.path.join(PASCAL_LABELS_DIR, filename)
        print(xml_path)

        f = open(xml_path, 'r')
        file = f.read()

        data = BeautifulSoup(file, "xml")

        filename = data.find('filename').text
        frame_number = int(filename.split('.')[0].split('_')[1].lstrip('0') or '0')

        xml_objects = data.find_all('object')

        for xml_object in xml_objects:
                xCoord = float(xml_object.find('xmin').text)
                yCoord = float(xml_object.find('ymin').text)
                height = float(xml_object.find('ymax').text) - yCoord
                width  = float(xml_object.find('xmax').text) - xCoord
                
                classId  = classes[xml_object.find('name').text]
                objectId = xml_object.find('attributes').find_all('attribute')[1].find('value').text            
                ts = FRAME_TIME*frame_number

                box = np.zeros(1, dtype=EventBbox)
                box["t"] = ts
                box["x"] = xCoord
                box["y"] = yCoord
                box["w"] = width
                box["h"] = height
                box["class_id"] = classId
                box["track_id"] = objectId
                box["class_confidence"] = 1
                list_boxes.append(box.copy())
                txt.write((('%s %s %s %s %s %s %s\n')%(ts, objectId, classId, xCoord, yCoord, height, width)))
    boxes_array = np.concatenate(list_boxes)
    print(boxes_array.shape)

###############################
save_filename = PASCAL_LABELS_DIR.split('/')[-2]
np.save('/home/exx/Documents/aayush/scripts/labels_output/nighttime/' + save_filename + '_bbox.npy', boxes_array)

