#Ŀ�ģ����ļ����еı�ǩͼ��ŵ�һ��
#˼·�������ļѼ��е�����label.png�����临�Ʒŵ���һ���ļ��в���������
#


import os
import shutil

dir_path="C:/Users/chenkj/Desktop/afterLabel/all"           #ԭ�ļ���·��
newPath="C:/Users/chenkj/Desktop/unet/imgs"         #���ļ���·��
newPath2="C:/Users/chenkj/Desktop/unet/masks"

fileNames=os.listdir(dir_path)
img_list=[]

for file in fileNames:              #�����ļ���
    img_folder=dir_path+'/'+file    #�ļ����е��ļ���
    print(img_folder)

    if os.path.exists(img_folder):                  #�ж��Ƿ���ڸ��ļ�
        for image_name in os.listdir(img_folder):   #�������ļ���
            #print(image_name)
            if(image_name=='label.png'):
                originPath=img_folder+'/'+image_name
                newfilePath=newPath2+'/'+file+'.png'
                shutil.copyfile(originPath,newfilePath)
            if(image_name=='img.png'):
                originPath2=img_folder+'/'+image_name
                newfilePath2=newPath+'/'+file+'.png'
                shutil.copyfile(originPath2,newfilePath2)
print('ok')




 

