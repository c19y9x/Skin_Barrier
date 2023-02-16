# 相关图
# 相关图是直方图，它不仅衡量图像特征的统计量，还考虑这些特征的空间分布。在这项工作中，为图像的 ROI 实现了两个相关图：
# 1.基于像素灰度值分布距离图像中心的距离
# 2.根据它们的分布角度。
# 对于每个像素，计算与图像中心的距离和角度，并且对于具有相同距离或角度的所有像素，计算它们的直方图。
# 为了使不同大小的图像之间的比较可行，对距离相关图进行了归一化。
# 允许相关图的角度在从图像的左中间开始并顺时针移动的可能值之间变化。得到的相关图是矩阵。

# Hd, Ht, labels = correlogram(f, mask, bins_digitize=32, bins_hist=32, flatten=True)
# 未完成

import os, sys
sys.path.append(os.getcwd())
import pyfeats
import numpy as np
from PIL import Image
import utils
import pandas as pd
import pickle
from tqdm import tqdm

def load_image(image_path):
    # 读取图像
    # image_path = 'My_image/group_tape_stripping_numbers/3_20_0/3_0_20_0.jpg'
    image = Image.open(image_path)
    # 转换为灰度图像
    image = image.convert('L')
    # 转换为numpy数组
    image = np.array(image)
    return image

dir_path = "My_image/group_tape_stripping_numbers"
img_feature_list_features_Hd = []
img_feature_list_features_Ht = []
img_name_list = []
colunms = []

# 增加TEWL值
f1 = open('TEWL.pkl','rb')
tewl_list = pickle.load(f1)
f1.close()
images_path1 = utils.get_file_list(dir_path)
for i,image_path1 in tqdm(enumerate(images_path1),total=len(images_path1)):
    images_path2 = utils.get_file_list(dir_path +"/" + image_path1)
    for image_path2 in images_path2:
        image = load_image(dir_path +"/" + image_path1 +"/" + image_path2)
        # 创建遮罩对象
        mask_zero = np.zeros(image.shape, dtype=np.uint8)
        mask_one = np.ones(image.shape, dtype=np.uint8)
        # mask_zero[image.shape[0]/4:3*image.shape[0]/4,image.shape[1]/4:3*image.shape[1]/4] = 1
        mask_zero[120:360,160:480] = 1
        # print(mask_one)
        # 提取特征
        features_Hd, features_Ht, labels = pyfeats.correlogram(image, mask_zero,bins_digitize=8, bins_hist=8, flatten=True)

        # Hd
        features_Hd = features_Hd.tolist()
        features_Hd.append(float(tewl_list[image_path2]))
        img_feature_list_features_Hd.append(features_Hd)
        
        # Ht
        features_Ht = features_Ht.tolist()
        features_Ht.append(float(tewl_list[image_path2]))
        img_feature_list_features_Ht.append(features_Ht)

        img_name_list.append(image_path2)
        # print("%s提取完成" % image_path2)

    if i == 0:
        labels.append("TEWL")
        colunms.append(labels)


    

output_excel_Hd = "Result/xls/"+os.path.basename(__file__).split('.')[0]+"_features_Hd_ROI.xls"
output_excel_Ht = "Result/xls/"+os.path.basename(__file__).split('.')[0]+"_features_Ht_ROI.xls"
img_info_df_Hd = pd.DataFrame(columns=colunms)
img_info_df_Ht = pd.DataFrame(columns=colunms)
for i in range(len(img_feature_list_features_Hd)):
    img_info_df_Hd.loc[img_name_list[i]] = img_feature_list_features_Hd[i]
for i in range(len(img_feature_list_features_Ht)):
    img_info_df_Ht.loc[img_name_list[i]] = img_feature_list_features_Ht[i]
# 输出统计特征
writer_Hd = pd.ExcelWriter(output_excel_Hd)
writer_Ht = pd.ExcelWriter(output_excel_Ht)
img_info_df_Hd.to_excel(writer_Hd, index=True, float_format="%.5f")
img_info_df_Ht.to_excel(writer_Ht, index=True, float_format="%.5f")
writer_Hd.save()
writer_Ht.save()