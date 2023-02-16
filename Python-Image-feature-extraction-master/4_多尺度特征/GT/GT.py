# 图像的 Gabor 变换 (GT) 在于将该图像与 Gabor 函数进行卷积，即由高斯包络调制的特定频率和方向的正弦平面波。 
# Gabor 滤波器的频率和方向表示类似于人类视觉系统的表示，使它们适用于纹理分割和分类。
# GT特征如下：1）均值和2）图像GT的细节子图像的绝对值的标准偏差。

# 结果没跑出来

# features, labels = gt_features(f, mask, deg=4, freq=[0.05, 0.4])

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
img_feature_list = []
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
        features, labels = pyfeats.gt_features(image, mask_one,deg=4, freq=[0.05, 0.4])
        # print(features,labels)
        features = features.tolist()
        features.append(float(tewl_list[image_path2]))
        img_feature_list.append(features)
        img_name_list.append(image_path2)
        # print("%s提取完成" % image_path2)

    if i == 0:
        labels.append("TEWL")
        colunms.append(labels)

    
    
output_excel = os.path.basename(__file__).split('.')[0]+"_features_无遮罩.xls"
img_info_df = pd.DataFrame(columns=colunms)
for i in range(len(img_feature_list)):
    img_info_df.loc[img_name_list[i]] = img_feature_list[i]
# 输出统计特征
writer = pd.ExcelWriter(output_excel)
img_info_df.to_excel(writer, index=True, float_format="%.5f")
writer.save()