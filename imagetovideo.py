
# -------------------------------------------- 
# __author__ : Dnyaneshwar Dewadkar 
#            : 10:05 AM 29/07/20
#            : imagetovideoconverter.py 
#  
# --------------------------------------------


import cv2
import numpy as np


import glob


size =(1024, 1024)
img_array = []
counter = 0
for filename in glob.glob('../wheat_data/train/*.jpg'):
    if counter > 500:
        break
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)
    counter = counter + 1
out = cv2.VideoWriter('project500.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()



