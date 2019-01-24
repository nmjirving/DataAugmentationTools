import xml.etree.ElementTree as ET
import os
import cv2

xml_file = '/media/ubtu/TOSHIBA EXT/medicineBox/rot_xmls/000000_rot8.xml'
tree = ET.parse(xml_file)
root = tree.getroot()
img_file = '/media/ubtu/TOSHIBA EXT/medicineBox/rot_imgs/000000_rot8.jpg'

im = cv2.imread(img_file)

for object in root.findall('object'):
    object_name = object.find('name').text
    Xmin = int(object.find('bndbox').find('xmin').text)
    Ymin = int(object.find('bndbox').find('ymin').text)
    Xmax = int(object.find('bndbox').find('xmax').text)
    Ymax = int(object.find('bndbox').find('ymax').text)

    color = (4, 250, 7)

    cv2.rectangle(im, (Xmin, Ymin), (Xmax, Ymax), color, 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(im, object_name, (Xmin, Ymin-7),
                font, 0.5, (6, 230, 230), 2)
    cv2.imshow('bbox visualize', im)

cv2.imwrite('/media/ubtu/TOSHIBA EXT/medicineBox/visualizeBbox/000000_rot8.jpg', im)

