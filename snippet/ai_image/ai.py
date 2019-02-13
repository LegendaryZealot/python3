import cv2 as cv
import numpy as np

def execute(img,model_path):
    w,h=img.shape[:2]
    inp = cv.dnn.blobFromImage(img, 1.0, (320, 480),(103.939, 116.779, 123.68), swapRB=False, crop=False)
    net = cv.dnn.readNetFromTorch(model_path)
    net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
    net.setInput(inp)
    out=net.forward()
    out = out.reshape(3, out.shape[2], out.shape[3])
    out[0] += 103.939
    out[1] += 116.779
    out[2] += 123.68
    out /= 255
    out = out.transpose(1, 2, 0)
    return out

if '__main__'==__name__:
    import sys
    import base64
    out=execute(cv.imread(sys.argv[1]),sys.argv[2])
    cv.imshow('raw',out)
    cv.imwrite('out.jpg',out)
    img=cv.imread('out.png',cv.IMREAD_COLOR)
    cv.imshow('out',img)
    img_encode=cv.imencode('.png',out)[1]
    with open('b64.txt','w') as f:
        f.write(str(base64.b64encode(img_encode))[2:-1])
    cv.waitKey(0)