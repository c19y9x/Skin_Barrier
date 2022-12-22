import os


# 删除文件夹下的所有文件
def delete_file(path):
    for i in os.listdir(path):
        file_path = os.path.join(path, i)
        if os.path.isfile(file_path):
            os.remove(file_path)
        # 删除文件夹
        elif os.path.isdir(file_path):
            delete_file(file_path)

delete_file("cyx")
# 切分文件路径
def split_path(path):
    path = path.replace("\\", "/")
    path_list = path.split("/")
    return path_list

filePath = "My_image/resize/3_50_90"
filepath1 = filePath.split("/")
print(filepath1)

