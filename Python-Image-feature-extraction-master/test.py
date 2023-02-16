
import random
import numpy as np
import pickle
import pandas as pd
import pymannkendall as mk
import re
import pyfeats
from PIL import Image
import os

def load_image(image_path):
    # 读取图像
    # image_path = 'My_image/group_tape_stripping_numbers/3_20_0/3_0_20_0.jpg'
    image = Image.open(image_path)
    # 转换为灰度图像
    image = image.convert('L')
    # image.show()
    # 转换为numpy数组
    image = np.array(image)
    return image

image = load_image("My_image/group_tape_stripping_numbers/3_20_0/3_0_20_0.jpg")
mask_one = np.ones(image.shape)
pyfeats.plot_histogram(image,mask_one,Ng=256,bins=32,name='sss')