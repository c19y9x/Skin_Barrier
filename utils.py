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


# 切分文件路径
def split_path(path):
    path = path.replace("\\", "/")
    path_list = path.split("/")
    return path_list

# 删除指定文件名的文件
def delete_file_name(path, file_name):
    for i in os.listdir(path):
        file_path = os.path.join(path, i)
        if os.path.isfile(file_path):
            if i == file_name:
                os.remove(file_path)
                print("删除文件：", file_path)
        else:
            delete_file_name(file_path, file_name)

# 迭代获取文件夹下的所有文件名
def get_file_name(path):
    file_name_list = []
    for i in os.listdir(path):
        file_path = os.path.join(path, i)
        if os.path.isfile(file_path):
            file_name_list.append(file_path)
        else:
            file_name_list.extend(get_file_name(file_path))
    return file_name_list


delete_file_name("My_image\group_tape_stripping_numbers","GLCMFeatures.png")


