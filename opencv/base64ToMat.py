import base64
import numpy as np
import cv2 as cv

def base64ToMat(base64_str,type_=cv.IMREAD_COLOR):
    img_data=base64.b64decode(base64_str)
    np_arr=np.fromstring(img_data,np.uint8)
    return cv.imdecode(np_arr,type_)

if '__main__'==__name__:
    import sys
    with open(sys.argv[1],'r') as f:
        img=base64ToMat(f.read())
        cv.imshow('[mat]',img)
        cv.waitKey(0)