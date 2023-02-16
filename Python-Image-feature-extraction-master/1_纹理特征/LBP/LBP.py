# 局部二进制模式 (LBP) 是一种鲁棒且高效的纹理描述符，由 Ojala 首次提出。 
# LBP 特征向量以其最简单的形式使用以下方法确定：在像素周围考虑圆形邻域。
# 在半径为 R 的圆的圆周上选择 P 个点，使它们都与中心像素等距。 
# 根据该像素的灰度值是小于还是大于中心像素的灰度值，将这些P点转换为0和1的循环比特流。奥贾拉等。 (2002) 
# 在纹理分析中引入了均匀性的概念。统一的基本模式具有统一的圆形结构，其中包含非常少的空间转换 U（空间按位 0/1 转换的数量）。
# 在这项工作中，计算了使用均匀性度量 U 的旋转不变度量。只有 U 小于 2 的模式才被分配 LBP 代码，即，如果循环比特流中的比特转换数小于或等于 2，
# 则中心像素被标记为均匀。在不同尺度上构建的 LBP 图像的能量和熵用作特征描述符。

# features, labels = lbp_features(f, mask, P=[8,16,24], R=[1,2,3])

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
        features, labels = pyfeats.lbp_features(image, mask_zero,P=[8,16,24], R=[1,2,3])
        features = features.tolist()
        features.append(float(tewl_list[image_path2]))
        img_feature_list.append(features)
        img_name_list.append(image_path2)
        # print("%s提取完成" % image_path2)
    if i == 0:
        labels.append("TEWL")
        colunms.append(labels)
    
output_excel = "Result/xls/"+os.path.basename(__file__).split('.')[0]+"_features_ROI.xls"
img_info_df = pd.DataFrame(columns=colunms)
for i in range(len(img_feature_list)):
    img_info_df.loc[img_name_list[i]] = img_feature_list[i]
# 输出统计特征
writer = pd.ExcelWriter(output_excel)
img_info_df.to_excel(writer, index=True, float_format="%.5f")
writer.save()