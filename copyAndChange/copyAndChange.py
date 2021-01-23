#Ŀ�ģ����ļ����еı�ǩͼ��ŵ�һ��
#˼·�������ļѼ��е�����label.png�����临�Ʒŵ���һ���ļ��в���������
#


import os
import shutil

dir_path="C:/Users/chenkj/Desktop/G3_1"           #ԭ�ļ���·��
newPath="C:/Users/chenkj/Desktop/G3_1/00"         #���ļ���·��

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
                newfilePath=newPath+'/'+file+'.png'
                shutil.copyfile(originPath,newfilePath)

print('ok')




 

