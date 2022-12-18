import matplotlib.pyplot as plt
from matplotlib.image import imread
import os

# 获取文件夹下的所有文件名
def get_file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files

# 显示图片
def show_image(file_dir):
    files = get_file_name(file_dir)
    for file in files:
        img = imread(file_dir +"\\" + file)
        plt.imshow(img)
        plt.show()

# 显示四张图片
def show_four_image(file_dir):

    files = get_file_name(file_dir)
    for i in range(4):
        img = imread(file_dir +"\\" + files[i])
        plt.subplot(2, 2, i+1)
        plt.imshow(img)
    plt.show()

if __name__ == '__main__':
    file_dir = 'cyx\\images'
    show_four_image(file_dir)
