import h5py
import hdf5plugin
import numpy as np
from PIL import Image

filep = '/media/exx/data/aayush/YOLO/10-47-27_s2_0.h5'


with h5py.File(filep, "r") as f1:

    for idx, img in enumerate(f1['data'][400:410]):
        channel1 = img[0,:,:]
        channel2 = img[1,:,:]
        channel3 = np.zeros_like(channel1)

        final_img = np.stack([channel1,channel2], axis=-1)

        # Creating an image from the modified array
        img = Image.fromarray(final_img)
        print(final_img.shape)
        img.save(f'img-{idx}.jpg')
        # break
        # Displaying the image
        


    # for key in evts.keys():
    #     dataset = evts[key]
    #     print(f"Dataset '{key}': Shape={dataset.shape}, Dtype={dataset.dtype}, Size={dataset.size * dataset.dtype.itemsize} bytes")


