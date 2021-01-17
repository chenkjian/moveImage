#目的：将文件夹中的标签图像放到一起
#思路：遍历文佳家中的所有label.png，将其复制放到另一个文件夹并重新命名
#


import os
import shutil

dir_path="C:/Users/chenkj/Desktop/G1"           #原文件夹路径
newPath="C:/Users/chenkj/Desktop/G1/00"         #新文件夹路径

fileNames=os.listdir(dir_path)
img_list=[]

for file in fileNames:              #遍历文件夹
    img_folder=dir_path+'/'+file    #文件夹中的文件名
    print(img_folder)

    if os.path.exists(img_folder):                  #判断是否存在该文件
        for image_name in os.listdir(img_folder):   #遍历子文件夹
            #print(image_name)
            if(image_name=='label.png'):
                originPath=img_folder+'/'+image_name
                newfilePath=newPath+'/'+file+'.png'
                shutil.copyfile(originPath,newfilePath)

print('ok')







