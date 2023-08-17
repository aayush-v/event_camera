import numpy as np

data = np.load('/home/exx/Documents/aayush/pipeline/detections/first_experiment/daytime_test/09-19-01_detections.npy')

print(data.shape)
print(data[:3])
print(data[-1])

data = np.load('/home/exx/Documents/aayush/currentData/raw_data/july27/label_bbox/detections/09-19-01_detections.npy')

print(data.shape)
print(data[:3])
print(data[-1])
# data = np.load('/home/exx/Documents/aayush/pipeline/dataset_folder/test/09-19-01_1_bbox.npy')

# print(':')
# print(data.shape)
# # print(data[8][5])
# class_map = {}

# for i in range(8):
#     class_map[i]=0

# for box in data:
#     class_map[box[5]]+=1

# print(class_map)

# data = np.load('/home/exx/Documents/aayush/pipeline/dataset_folder/test/10-47-27_s2_0_bbox.npy')

# print(':')
# print(data.shape)
# class_map = {}

# for i in range(8):
#     class_map[i]=0

# for box in data:
#     class_map[box[5]]+=1

# print(class_map)
