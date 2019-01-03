import cv2 as cv
import numpy as np
import sys
import os

def imgScale(path,scale):
    scale=float(scale)
    img=cv.imread(path)
    height, width = img.shape[:2]
    size = (int(width*scale), int(height*scale))
    if(scale>1):
        img = cv.resize(img, size, interpolation=cv.INTER_CUBIC)
    else:
        img = cv.resize(img, size, interpolation=cv.INTER_AREA)
    cv.imwrite(path,img)

if '__main__' == __name__:
    if(3!=len(sys.argv)):
        print('prara error(s):dir path,scale')
    else:
        for path in os.listdir(sys.argv[1]):
            path=os.path.join(sys.argv[1],path)
            if(os.path.isfile(path)):
                if(len(path)-4==path.find('.png')):
                    imgScale(path,sys.argv[2])
                else:
                    print('%s is not a png'%format(path))
            else:
                # print('%s is a dir'%format(path))
                pass