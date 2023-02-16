# GLRLM Gray Level Run Length Matrix 
# 灰度运行是一组具有相同灰度值的连续、共线的图像点。运行的长度是运行中的图片点数。 GLRLM 特征如下：
# 1) 短期运行强调，2) 长期运行强调，3) 灰度级不均匀性，4) 运行长度不均匀性，5) 运行百分比，6) 低灰度级运行强调，
# 7)高灰度强调，8) 短期低灰度强调， 9) 短期高灰度强调， 10) 长期低灰度强调， 11) 长期高灰度强调。

# GLRLM 算法使用基于灰度级对之间或平均灰度级之间的绝对差的局部属性值的一阶统计来提取纹理度量。
# GLRLM 算法的输入是灰度图像，输出是一个矩阵，矩阵的行表示灰度级，列表示运行长度。矩阵中的每个元素表示
# 一个灰度级和一个运行长度的组合。矩阵中的元素值表示图像中具有该灰度级和该运行长度的像素点的个数。

# features, labels = glrlm_features(f, mask, Ng=256)
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
        features, labels = pyfeats.glrlm_features(image, mask_zero, Ng=256)
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
