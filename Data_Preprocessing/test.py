
import pandas as pd
import numpy as np
import re
import pickle
# pandas读取xls文件


# 读取xls文件
df = pd.read_excel('Data_Preprocessing\TEWL对应数据.xlsx', index_col=0)
df1 = df.to_dict("dict")

data = df1['TEWL']
mouse_numbers = [3,4,12,51]           # 小鼠编号
tape_stripping_numbers = [0,2,4,6,8]  # 胶带剥离次数
fangda = [20,50]                      # 放大倍数
polarization = [0,90]                 # 是否偏振
shiyan_numbers = [0,1,2]              # 实验组号

# 数字列表转字符串
def list_to_str(list):
    str1 = []
    for i in list:
        str1.append(str(i))
    return str1

mouse_numbers = list_to_str(mouse_numbers)
tape_stripping_numbers = list_to_str(tape_stripping_numbers)
fangda = list_to_str(fangda)
polarization = list_to_str(polarization)


dict1 = {}
for i in mouse_numbers:
    for j in tape_stripping_numbers:
        for k in fangda:
            for l in polarization:
                    dict1[str(i)+'_'+str(j)+'_'+str(k)+'_'+str(l)+".jpg"] = []

                    
for filename in data.keys():
    filename_split = re.split(r'[_\.]',filename)
    # print(filename_split)
    # 验证文件名前四个数字是否规范
    if filename_split[0] in mouse_numbers and filename_split[1] in tape_stripping_numbers and filename_split[2] in fangda and filename_split[3] in polarization:
        dict1[filename_split[0]+'_'+filename_split[1]+'_'+filename_split[2]+'_'+filename_split[3]+".jpg"].append(data[filename])
    else:
        print(filename)


# 将值取平均值
for i in dict1.keys():
    dict1[i] = f'{np.mean(dict1[i]): .2f}' # 保留两位小数


# 将字典保存到pkl文件中
output = open('TEWL.pkl', 'wb')
pickle.dump(dict1, output)



