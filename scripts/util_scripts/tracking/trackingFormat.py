import numpy as np
import os
import glob


FREQUENCY = 33_333
# FREQUENCY = 50_000

def convertGTBboxToMOT16(boxes, dst_folder, file_name, offset, combined_fp, track_offset):
    max_track_num = 0
    
    with open(f'{dst_folder}/{file_name[:-4]}.txt', 'w') as file:
        for box in boxes:
            file.write(f"{int(box['t']/FREQUENCY)}, {box['track_id']}, {box['x']}, {box['y']}, {box['w']}, {box['h']}, {box['class_confidence']}, -1, -1, -1\n")
            combined_fp.write(f"{int(box['t']/FREQUENCY) + offset}, {box['track_id']+track_offset}, {box['x']}, {box['y']}, {box['w']}, {box['h']}, {box['class_confidence']}, -1, -1, -1\n")

            max_track_num = max(max_track_num, box['track_id'])

    return max_track_num



def convertTrackedBboxToMOT16(boxes, dst_folder, file_name, offset, combined_fp, track_offset):
    max_track_num = 0

    with open(f'{dst_folder}/{file_name[:-4]}.txt', 'w') as file:
        for box in boxes:
            tolerance = box['t']%FREQUENCY
            frame_num = 0

            if tolerance < 5_000:
                frame_num = int(box['t']/FREQUENCY)
            elif tolerance > 28_333:
                frame_num = int(box['t']/FREQUENCY) + 1
            else:
                continue

            file.write(f"{frame_num}, {box['track_id']}, {box['x']}, {box['y']}, {box['w']}, {box['h']}, {box['class_confidence']}, -1, -1, -1\n")
            combined_fp.write(f"{frame_num + offset}, {box['track_id'] + track_offset}, {box['x']}, {box['y']}, {box['w']}, {box['h']}, {box['class_confidence']}, -1, -1, -1\n")
            
            max_track_num = max(max_track_num, box['track_id'])

    return max_track_num


if __name__ == "__main__":
    src_folder_gt = '/media/exx/data/aayush/eTraM work/rebuttal/RED/GT'
    dst_folder_gt = '/media/exx/data/aayush/eTraM work/rebuttal/RED/GT/txt'

    src_folder_tracks = '/media/exx/data/aayush/eTraM work/rebuttal/RED/tracking'
    dst_folder_tracks = '/media/exx/data/aayush/eTraM work/rebuttal/RED/tracking/txt'

    gt = sorted(glob.glob(os.path.join(src_folder_gt, '**/*.npy'), recursive=True))
    tracks = sorted(glob.glob(os.path.join(src_folder_tracks, '**/*.npy'), recursive=True))

    gt_combined_fp = open(f'{dst_folder_gt}/combined_gt.txt', 'w')
    tracks_combined_fp = open(f'{dst_folder_tracks}/combined_tracks.txt', 'w')

    offset = 0
    tracking_gt_offset = 0
    tracking_tracked_offset = 0


    for idx in range(len(gt)):
        gt_file = np.load(gt[idx])
        tracks_file = np.load(tracks[idx])

        max_gt_track_num = convertGTBboxToMOT16(gt_file, dst_folder_gt, gt[idx].split('/')[-1], offset, gt_combined_fp, tracking_gt_offset)
        max_tracked_num = convertTrackedBboxToMOT16(tracks_file, dst_folder_tracks, tracks[idx].split('/')[-1], offset, tracks_combined_fp, tracking_tracked_offset)

        max_frame_num = max(gt_file[-1]['t'], tracks_file[-1]['t'])

        offset += int(max_frame_num/FREQUENCY) + 2
        tracking_gt_offset += max_gt_track_num + 2
        tracking_tracked_offset += max_tracked_num + 2

        print(offset, tracking_gt_offset, tracking_tracked_offset)


