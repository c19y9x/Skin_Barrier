import os
import re
import shutil 
import random
import utils

# 获取当前时间
import time
import datetime
now = datetime.datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))

log_file = open("skin_TDA-master/src/操作记录.txt", 'a')

path = "skin_TDA-master/Image/1209/photo"


# 检查3号小鼠不规范的命名
file_list = utils.get_file_list(path)
file_list1 = {} # 用于存放待修改的文件名
for file in file_list:
    filename = re.split('[\._]', file)
    if filename[5] == 'jpg':
        if filename[4] != '3':
            utils.delete_file(path, file)
            log_file.write(now.strftime('%Y-%m-%d %H:%M:%S')+'删除文件：' + file +'\n' )
            continue   
        utils.rename_file(path, file, filename[0]+'_'+filename[1]+'_'+filename[2]+'_'+filename[3] +'_'+ filename[4] + '_0' + '.jpg')
        log_file.write(now.strftime('%Y-%m-%d %H:%M:%S')+'修改文件：' + file + '为' + filename[0]+'_'+filename[1]+'_'+filename[2]+'_'+filename[3] +'_'+ filename[4] + '_0' + '.jpg'+'\n')

# 检查文件名段是否为7
# file_list = utils.get_file_list(path)
# for file in file_list:
#     filename = re.split('[\._]', file) 
#     if len(filename) != 7:
#         print(filename)

# 数据扩充 
# file_list = utils.get_file_list(path)
# file_list1 = {}
# for file in file_list:
#     filename = re.split('_\d_\d\.jpg', file)
#     file_list1[filename[0]] = file_list1[filename[0]] + 1 if filename[0] in file_list1 else 0
    

# for key,value in file_list1.items():
#     if value < 2:
#         log_file.write(key+'缺少文件'+'\n')
#         if value == 1:
#             utils.copy_file(path, key+'_3_'+ str(random.randint(0,1))+'.jpg', key+'_3_2.jpg')
#             log_file.write(now.strftime('%Y-%m-%d %H:%M:%S')+' 复制文件：' + key+'_3_'+ str(random.randint(0,1))+'.jpg' + '为' + key+'_3_2.jpg'+'\n')
#         else:
#             utils.copy_file(path, key+'_3_0'+'.jpg', key+'_3_1.jpg')
#             log_file.write(now.strftime('%Y-%m-%d %H:%M:%S')+' 复制文件：' + key+'_3_0'+'.jpg' + '为' + key+'_3_1.jpg'+'\n')
#             utils.copy_file(path, key+'_3_0'+'.jpg', key+'_3_2.jpg')
#             log_file.write(now.strftime('%Y-%m-%d %H:%M:%S')+' 复制文件：' + key+'_3_0'+'.jpg' + '为' + key+'_3_2.jpg'+'\n')
#     else:
#         log_file.write(key+'正常不缺少'+'\n')

# 检查是否哪组图像不为3张
# file_list = utils.get_file_list(path)
# file_list1 = {}
# for file in file_list:
#     filename = re.split('_\d_\d\.jpg', file)
#     file_list1[filename[0]] = file_list1[filename[0]] + 1 if filename[0] in file_list1 else 0
# for key,value in file_list1.items():
#     if value != 2:
#         print(key+'不为3张'+'\n')





log_file.close()


