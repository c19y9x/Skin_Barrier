import re
import shutil 
import random
import numpy as np
import pandas as pd
import pywt,cv2,sys,subprocess,os
import matplotlib.pyplot as plt

# 获取文件夹下的文件列表
def get_file_list(path):
    file_list = []
    for file in os.listdir(path):
        # file_path = os.path.join(file)
        # if os.path.isfile(file_path):
        file_list.append(file)
    return file_list

# 删除指定扩展名的文件
def delete_file_withext(path, ext):
    file_list = get_file_list(path)
    for file in file_list:
        if file.endswith(ext):
            os.remove(os.path.join(path,file))
# delete_file_withext('1209\photo', '.cmf')

# 分割文件名
def split_file_name(file_name):
    file_name = file_name.split('.')
    return file_name[0], file_name[1]

# 重命名文件
def rename_file(path, old_name, new_name):
    old_file = os.path.join(path, old_name)
    new_file = os.path.join(path, new_name)
    os.rename(old_file, new_file)


# 同文件夹复制文件
def copy_file(path, old_name, new_name):
    old_file = os.path.join(path, old_name)
    new_file = os.path.join(path, new_name)
    shutil.copy(old_file, new_file)

# 写入txt文件
def write_txt(path, file_name, content):
    file = open(os.path.join(path, file_name), 'w')
    file.write(content)
    file.close()

# 删除文件
def delete_file(path, file_name):
    file = os.path.join(path, file_name)
    os.remove(file)

# 修改图像尺寸
def resize_image(image_path, output_path, width, height):
    imArray = cv2.imread(image_path)
    imArray = cv2.resize(imArray, dsize=(width, height))
    cv2.imwrite(output_path, imArray)

# 计算output.txt
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

# log_file = open("操作记录.txt", 'a')
# # 修改不规范名称

# path = "1209\photo"
# file_list = get_file_list(path)
# file_list1 = {} # 用于存放待修改的文件名
# for file in file_list:
#     filename = re.split('[\._]', file)
#     if filename[5] == 'jpg':

#         file_list1[filename[0]+filename[1]+filename[2]+filename[3]] = file_list1[filename[0]+filename[1]+filename[2]+filename[3]] \
#         + 1 if filename[0]+filename[1]+filename[2]+filename[3] in file_list1 else 0
#         rename_file(path, file, filename[0]+'_'+filename[1]+'_'+filename[2]+'_'+filename[3] + '_' + str(int(filename[5])+1) + '.jpg')

#         print(filename)



# 检查是否规范

# path = "1209\photo"
# file_list = get_file_list(path)
# for file in file_list:
#     filename = re.split('[\._]', file)
#     if filename[4] != '3':
#        print(filename)



# 数据扩充
# path = "1209\photo"
# file_list = get_file_list(path)
# file_list1 = {} # 用于存放待修改的文件名
# for file in file_list:
#     filename = re.split('[\._]', file)
#     file_list1[filename[0]+filename[1]+filename[2]+filename[3]] = file_list1[filename[0]+filename[1]+filename[2]+filename[3]] \
#     + 1 if filename[0]+filename[1]+filename[2]+filename[3] in file_list1 else 0
    
#     print(filename)


# 统计文件名称
# path = "1209\photo"
# file_list = get_file_list(path)
# file_list1 = {} # 用于存放待修改的文件名
# for file in file_list:
#     filename = re.split('_[012]\.jpg', file)
#     # if filename[5] == 'jpg':
#     file_list1[filename[0]] = file_list1[filename[0]] \
#     + 1 if filename[0] in file_list1 else 1
# print(file_list1)
# for key, value in file_list1.items():
#     if value < 3:
#         # for i in range(3-value):
#         #     copy_file(path, key + '_1.jpg', key + '_' + str(value+1) + '.jpg')
#         #     value = value + 1
#         print(key.split())

# log_file.close()
