import numpy as np
import os
import glob


FREQUENCY = 33_333
# FREQUENCY = 50_000

def convertGTBboxToMOT16(boxes, dst_folder, file_name):
    
    with open(f'{dst_folder}/{file_name}.txt', 'w') as file:
        i = 0
        for box in boxes:
            # print(box)
            file.write(f"{box['t']/FREQUENCY}, {box['track_id']}, {box['x']}, {box['y']}, {box['w']}, {box['h']}, {box['class_confidence']}, -1, -1, -1\n")
            
            i+=1




def convertTrackedBboxToMOT16(boxes, dst_folder, file_name):
    
    with open(f'{dst_folder}/{file_name}.txt', 'w') as file:
        i = 0
        for box in boxes:
            tolerance = box['t']%FREQUENCY
            # print(box['t'])
            if tolerance < 5_000:
                file.write(f"{int(box['t']/FREQUENCY)}, {box['track_id']}, {box['x']}, {box['y']}, {box['w']}, {box['h']}, {box['class_confidence']}, -1, -1, -1\n")
            elif tolerance > 28_333:
                file.write(f"{int(box['t']/FREQUENCY)+1}, {box['track_id']}, {box['x']}, {box['y']}, {box['w']}, {box['h']}, {box['class_confidence']}, -1, -1, -1\n")
            i+=1

            
        
            

if __name__ == "__main__":
    pass

    src_folder_gt = '/media/exx/data/aayush/eTraM work/rebuttal/temp/gt'
    dst_folder_gt = '/media/exx/data/aayush/eTraM work/rebuttal/temp/MOT16_test/gt'

    src_folder_tracks = '/media/exx/data/aayush/eTraM work/rebuttal/temp/track_test'
    dst_folder_tracks = '/media/exx/data/aayush/eTraM work/rebuttal/temp/MOT16_test/tracks'

    gt = glob.glob(os.path.join(src_folder_gt, '**/*.npy'), recursive=True)
    tracks = glob.glob(os.path.join(src_folder_tracks, '**/*.npy'), recursive=True)

    for file in gt:
        boxes = np.load(file)
        convertGTBboxToMOT16(boxes, dst_folder_gt, file.split('/')[-1])
    

    for file in tracks:
        boxes = np.load(file)
        convertTrackedBboxToMOT16(boxes, dst_folder_tracks, file.split('/')[-1])


