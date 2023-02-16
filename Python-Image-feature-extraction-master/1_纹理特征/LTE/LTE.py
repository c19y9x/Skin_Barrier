# Law 的纹理能量测度，源自三个长度为 3 的简单向量。如果将这些向量与自身进行卷积，则会获得长度为 5 的新向量。
# 通过进一步自卷积，得到长度为7的新向量。如果长度为l的列向量乘以相同长度的行向量，则得到Laws l×l masks。
# 为了从图像中提取纹理特征，将这些掩码与图像进行卷积，并使用所得图像的统计信息（例如能量）来描述纹理：
# 1）来自 LL 内核的纹理能量，2）来自 EE 的纹理能量内核，3）来自 SS 内核的纹理能量，
# 4）来自 LE 和 EL 内核的平均纹理能量，5）来自 ES 和 SE 内核的平均纹理能量，6）来自 LS 和 SL 内核的平均纹理能量。

# features, labels = lte_measures(f, mask, l=7)

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
        features, labels = pyfeats.lte_measures(image, mask_zero, l = 7)
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