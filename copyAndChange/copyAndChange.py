# -*- coding:utf-8 -*-
 
import os
import random
class ImageRename():
    def __init__(self):
        self.path = 'C:\\Users\\chenkj\\Desktop\\old'#图片所在文件夹
 
    def rename(self):
        filelist = os.listdir(self.path)
        random.shuffle(filelist)
        total_num = len(filelist)
 
        i = 0
 
        for item in filelist:
            if item.endswith('.png'):
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), '0000' + format(str(i), '0>3s') + '.png')
                os.rename(src, dst)
                print ('converting %s to %s ...' % (src, dst))
                i = i + 1
        print ('total %d to rename & converted %d pngs' % (total_num, i))
 
if __name__ == '__main__':
    newname = ImageRename()
    newname.rename()