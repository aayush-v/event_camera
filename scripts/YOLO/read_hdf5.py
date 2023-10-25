import h5py
import hdf5plugin
import numpy as np
from PIL import Image
import glob
import os
# filep = '/media/exx/data/aayush/YOLO/10-47-27_s2_0.h5'

def createYOLOImages(filep):

    with h5py.File(filep, "r") as f1:
        directory_path = f'/media/exx/data/aayush/YOLO/dataset1/night/{filep.split("/")[-1][:-3]}'
        
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            print(f'Directory "{directory_path}" created successfully.')
        else:
            print(f'Directory "{directory_path}" already exists.')

        for idx, img in enumerate(f1['data']):
            channel1 = img[0,:,:]
            channel2 = img[1,:,:]
            channel3 = np.zeros_like(channel1)

            final_img = np.stack([channel1,channel2, channel3], axis=-1)
            final_img = (final_img * 255).astype('uint8')

            img = Image.fromarray(final_img)
            image_file_name = f"frame_{idx:06d}.png"
            img.save(os.path.join(directory_path, image_file_name))


if __name__ == "__main__":
        preprocessed_files = "/media/exx/data/aayush/YOLO/SAE_preproc/night"
        h5_files = glob.glob(os.path.join(preprocessed_files, '*.h5'))

        for file in h5_files:
            createYOLOImages(file)

