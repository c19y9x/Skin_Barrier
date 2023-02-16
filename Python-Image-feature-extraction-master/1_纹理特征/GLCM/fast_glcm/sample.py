# coding: utf-8

import numpy as np
from skimage import data
from matplotlib import pyplot as plt
import fast_glcm
import cv2,os

def main():
    pass

# 获取文件夹下的文件列表
def get_file_list(path):
    file_list = []
    for file in os.listdir(path):
        # file_path = os.path.join(file)
        # if os.path.isfile(file_path):
        file_list.append(file)
    return file_list

def show_image(path):
    img = cv2.imread(path ,cv2.IMREAD_GRAYSCALE)

    glcm_mean = fast_glcm.fast_glcm_mean(img)
    glcm_std = fast_glcm.fast_glcm_std(img)
    gclm = fast_glcm.fast_glcm(img)
    glcm_contrast = fast_glcm.fast_glcm_contrast(img)
    glcm_dissimilarity = fast_glcm.fast_glcm_dissimilarity(img)
    glcm_homogeneity = fast_glcm.fast_glcm_homogeneity(img)
    glcm_ASM = fast_glcm.fast_glcm_ASM(img)
    glcm_entropy = fast_glcm.fast_glcm_entropy(img)


    plt.figure(figsize=(12, 8))
    # plt.suptitle()
    plt.subplot(3, 3, 1)
    plt.title(path.split("/")[3])
    plt.imshow(img, cmap="gray")
    plt.subplot(3, 3, 2)
    plt.title("glcm std")
    plt.imshow(glcm_std)
    plt.subplot(3, 3, 3)
    plt.title("glcm mean")
    plt.imshow(glcm_mean)
    plt.subplot(3, 3, 4)
    plt.title("glcm contrast")
    plt.imshow(glcm_contrast)
    plt.subplot(3, 3, 5)
    plt.title("glcm entropy")
    plt.imshow(glcm_entropy)
    plt.subplot(3, 3, 6)
    plt.title("glcm homogeneity")
    plt.imshow(glcm_homogeneity)
    # plt.subplot(3, 3, 8)
    # plt.title(path.split("/")[3])
    # plt.imshow(glcm_entropy)
    
    
    plt.tight_layout()

    # 分割字符串，取第四个元素，即文件名
    plt.savefig("Result_Images/GLCM/GLCM_image/"+path.split("/")[3])
    # plt.show()

    

if __name__ == '__main__':
    main()

    path = "My_image/group_tape_stripping_numbers/3_50_90"
    file_list = get_file_list(path)
    for file in file_list:
        file_path = path+"/"+file
        show_image(file_path)
    # show_image("My_image/group_tape_stripping_numbers/3_20_90/3_8_20_90.jpg")

