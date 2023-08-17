from bs4 import BeautifulSoup
import numpy as np
import os
import glob
import xml.etree.ElementTree as ET


FPS = 30
FRAME_TIME = int(1000000/FPS)
PASCAL_LABELS_DIR = '/home/exx/Documents/aayush/main/labels_int/Annotations/'
REDUCTION_FACTOR = 1280/1920

########################################

filelist = glob.glob(os.path.join(PASCAL_LABELS_DIR, '*.xml'))

for filename in sorted(filelist):
    tree = ET.parse(filename)
    root = tree.getroot()

    # Find all <xmin> tags
    xmin_elements = root.findall(".//xmin")
    xmax_elements = root.findall(".//xmax")
    ymin_elements = root.findall(".//ymin")
    ymax_elements = root.findall(".//ymax")


    # Update the value of each <xmin> tag
    for xmin_element in xmin_elements:
        original_value = float(xmin_element.text)
        new_value =  REDUCTION_FACTOR * original_value
        xmin_element.text = str(new_value)

    # Update the value of each <xmin> tag
    for xmax_element in xmax_elements:
        original_value = float(xmax_element.text)
        new_value =  REDUCTION_FACTOR * original_value
        xmax_element.text = str(new_value)

    # Update the value of each <xmin> tag
    for ymin_element in ymin_elements:
        original_value = float(ymin_element.text)
        new_value =  REDUCTION_FACTOR * original_value
        ymin_element.text = str(new_value)

    # Update the value of each <xmin> tag
    for ymax_element in ymax_elements:
        original_value = float(ymax_element.text)
        new_value =  REDUCTION_FACTOR * original_value
        ymax_element.text = str(new_value)

    # Save the changes back to the XML file
    tree.write(filename)
    print("Update successful.")