import os,re,random
import subprocess
import utils
from tqdm import tqdm
import shutil


# Python运行R语言文件
def run_r_file(r_file_path):
    subprocess.run(r_file_path, shell=True)


filePath = '1209/photo' # 原始图像
fileResizePath = 'resize' # 修改尺寸后的图像


# 获取图像列表
# file_list = utils.get_file_list(filePath)
# 修改图像尺寸并保存
# for file in tqdm(file_list):
#     image_path = filePath + "/" + file
#     # 这里必须要新建一个文件夹，不然会报错
#     output_path = "resize/" + file
#     utils.resize_image(image_path, output_path, 1400, 1200)

# 计算output.txt
# file_list_resizeImage = utils.get_file_list(fileResizePath)
# for file in tqdm(file_list_resizeImage):
#     image_path = "resize/" + file
#     coordinate_data_path = "output/" + os.path.splitext(file)[0]+'.txt'
#     utils.preprocess(image_path, coordinate_data_path)

# 随机抽取文件进行仿真
# file_list_output = utils.get_file_list('output')
# file_list1 = {}
# mouse_numbers = [3,4,12,51]           # 小鼠编号
# tape_stripping_numbers = [0,2,4,6,8]  # 胶带剥离次数
# fangda = [20,50]                      # 放大倍数
# polarization = [0,90]                 # 是否偏振
# shiyan_numbers = [0,1,2]              # 实验组号

# for file in file_list_output:
#     filename = re.split('_\d_\d\.txt', file)
#     file_list1[filename[0]] = file_list1[filename[0]] + 1 if filename[0] in file_list1 else 0

# for i in mouse_numbers:
#     for j in polarization:
#         for k in fangda:
#             # 新建文件夹
#             new_path = '实验中途数据/' + str(i) + '_' + str(k) + '_' + str(j)
#             if not os.path.exists(new_path):
#                 os.makedirs(new_path)
#             for l in tape_stripping_numbers:
#                 # 随机抽取文件
#                 shutil.copy('output/'+ str(i) + '_' + str(l) + '_' + str(k) + '_' + str(j)+'_3_'+str(random.choice(shiyan_numbers))+'.txt', \
#                     new_path + '/' + str(i) + '_' + str(l) + '_' + str(k) + '_' + str(j) +'.txt')

file_list_output = utils.get_file_list('实验中途数据')
for file in tqdm(file_list_output):
    subprocess.run('Rscript merge_diagrams.R 实验中途数据/' + file, shell=True)

                