import numpy as np
import cv2 as cv

def fileToMat(file_path):
    with open(file_path,'rb') as f:
        np_arr=np.frombuffer(f.read(),np.uint8)
        return cv.imdecode(np_arr,cv.IMREAD_COLOR)  

if '__main__'==__name__:
    import sys
    mat=fileToMat(sys.argv[1])
    cv.imshow('[mat]',mat)
    cv.waitKey(0)