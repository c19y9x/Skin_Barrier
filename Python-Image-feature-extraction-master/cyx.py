import cv2
import numpy as np
from matplotlib import pyplot as plt


def plot(image):
    plt.hist(image.ravel(),256,[0,256])
    plt.show("matlab自带直方图")

def hist(image):
    color = ('blue','green','red')
    for i,color in enumerate(color):
        hist = cv2.calcHist([image],[i],None,[256],[0,256])
        plt.plot(hist,color=color)
        plt.xlim([0,256])
    plt.show()

import cv2
import imutils
 
img = cv2.imread("My_image/group_tape_stripping_numbers/3_20_0/3_0_20_0.jpg")
img = imutils.resize(img, width=500)
 
roi = cv2.selectROI(windowName="roi", img=img, showCrosshair=True, fromCenter=False)
x, y, w, h = roi

print(x, y, w, h)

imgROI = img[y:y+h, x:x+w].copy()  # 切片获得裁剪后保留的图像区域
print(img.shape,imgROI.shape)
cv2.imshow("roi", imgROI)


cv2.waitKey(0)
cv2.destroyAllWindows()


