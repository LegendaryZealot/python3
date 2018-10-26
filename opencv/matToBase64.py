import base64
import numpy as np
import cv2 as cv

def matToBase64(mat,type_='.jpg'):
    img_encode=cv.imencode(type_,mat)[1]
    return str(base64.b64encode(img_encode))[2:-1]

if '__main__'==__name__:
    import sys
    test=cv.imread(sys.argv[1])
    print(matToBase64(test))