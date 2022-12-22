import cv2,os
import matplotlib as plt

def resize_image(image_path, output_path, width, height):
    imArray = cv2.imread(image_path)
    imArray = cv2.resize(imArray, dsize=(width, height))
    cv2.imwrite(output_path, imArray)

# image_path="skin_diagram/2-4.jpg"
# imArray = cv2.imread(image_path)
# #trim the image to 1200*1400
# resize_img = cv2.resize(imArray, dsize=(1400, 1200))
# cv2.imwrite("save4.jpg", resize_img)

filePath = "My_image/3_50_90"
name = os.listdir(filePath)
for i in name:
    image_path = filePath + "/" + i
    # 这里必须要新建一个文件夹
    output_path = "My_image/resize/3_50_90/" + i
    resize_image(image_path, output_path, 1400, 1200)
