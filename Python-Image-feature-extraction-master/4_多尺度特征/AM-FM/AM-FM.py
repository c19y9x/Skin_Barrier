# 振幅调制 - 频率调制 (AM-FM)
# 我们考虑在最小二乘近似下对图像进行多尺度调幅-调频 (AM-FM) 表示。
# 对于每个图像，计算特定组件的瞬时振幅 (IA)、瞬时相位 (IP) 和瞬时频率 (IF)。
# 给定输入离散图像，我们首先应用希尔伯特变换以形成一维解析信号的二维扩展。
# 结果通过一组具有所需比例的带通滤波器进行处理。每个处理块将产生 IA、IP 和 IF。 
# AM-FM 特征如下：1) 低、2) 中、3) 高和 4) 直流重建图像的直方图。

# 结果没跑出来

# features, labels = amfm_features(f, bins=32)
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
        features, labels = pyfeats.amfm_features(image, bins=32)
        # print(features,labels)
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