import numpy as np
import pandas as pd
import pywt,cv2,sys,subprocess,os
import matplotlib.pyplot as plt

def preprocess(image_path, coordinate_data_path, min_wavelet_level=3, max_wavelet_level=10, erosion_times=5):
	imArray = cv2.imread(image_path)
	#trim the image to 1200*1400
	imArray = imArray[0:1200,0:1400]
	#transform to grayscale
	imArray = cv2.cvtColor(imArray, cv2.COLOR_BGR2GRAY)
	#transform to float (0~1)
	imArray =  np.float32(imArray)   
	imArray /= 255
	#calculate wavelet coefficients (Haar base)
	mode = "haar"
	coeffs=pywt.wavedec2(imArray, mode, level=8)
	#abandon coefficients of specified levels 放弃指定级别的系数
	coeffs_H=list(coeffs)
	if 0 < min_wavelet_level:
		coeffs_H[0] *= 0
	for i in range(11):
		if (i < min_wavelet_level or i > max_wavelet_level):
			coeffs_H[i] = tuple([np.zeros_like(v) for v in coeffs_H[i]])
	#reconstruct the image
	imArray_H=pywt.waverec2(coeffs_H, mode)
	imArray_H *= 255
	imArray_H =  np.uint8(imArray_H)
	#binarize the image using Otsu's method
	_,thr = cv2.threshold(imArray_H,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	#morphological operations
	#set the kernel
	kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
	#erode the white region several times 多次侵蚀白色区域
	binary_image = cv2.erode(thr, kernel, iterations = erosion_times)
	#get coordinates of white pixels 获取白色像素的坐标
	y,x = binary_image.nonzero()
	white_pixels = np.array([x,y])
	white_pixels = white_pixels.T
	#output
	np.savetxt(coordinate_data_path, white_pixels,fmt="%.0f",delimiter=",")

# 得到output.txt
filePath = "resize"
name = os.listdir(filePath)
for i in name:
    image_path = filePath + "/" + i
    output_path = "cyx/output_txt/" + os.path.splitext(i)[0]+".txt"
    preprocess(image_path, output_path)

# 读取output.txt 得到output0.txt output1.txt
R_script_path = "cyx/RTDA_cyx.R"
filePath = "cyx/output_txt"
name = os.listdir(filePath)
for i in name:
    output_txt_path = filePath + "/" + i
    output0_path = "cyx/output0_1_txt/" + os.path.splitext(i)[0]+"output0.txt"
    output1_path = "cyx/output0_1_txt/" + os.path.splitext(i)[0]+"output1.txt"
    subprocess.call("Rscript " + R_script_path + " " + output_txt_path + " " + output0_path + " " +  output1_path, shell = True)

# 制图
# filePath = "cyx/output0_1_txt"

# Rscript cyx/draw_images/draw_diagrams_birth_death.R cyx/output0_1_txt/2_0_20_0output0.txt