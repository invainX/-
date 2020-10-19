from tkinter import *
from tkinter.messagebox import *
import random
from PIL import Image, ImageTk
import os
import pygame, sys, random
from PIL.ImageTk import PhotoImage
from pygame.locals import *
import cv2operator
import os


# 分割成九张小图片
def splitimage(sre, rownum, colnum, dstpath):
    img = Image.open(src)
    (x, y) = img.size  # read image size
    x_s = gameRect.width * 2  # define standard width
    y_s = gameRect.height * 2  # calc height based on standard width
    img = img.resize((x_s, y_s), Image.ANTIALIAS)  # resize image with high-quality
    w, h = img.size  # 图片大小
    if rownum <= h and colnum <= w:
        print('original image info:%sx%s,%s,%s' % (w, h, img.format, img.mode))
        print('开始处理图片切割，请稍候-')
        s = os.path.split(src)
        if dstpath == '':  # 没有输入路径
            dstpath = s[0]  # 使用源图片所在目录s[0]
        fn = s[1].split('.')  # s[1]是源图片文件名
        basename = fn[0]  # 主文件名
        ext = fn[-1]  # 扩展名
        num = 0
        rowheight = (gameRect.width * 2 - 1) // rownum
        colwidth = (gameRect.height * 2 - 1) // colnum
        for r in range(rownum):
            for c in range(colnum):
                box = (c * colwidth, r * rowheight, (c + 1) * colwidth, (r + 1) * rowheight)
                img.crop(box).save(os.path.join(dstpath, basename + '' + str(num) + '.' + ext))
                num = num + 1
        print('图片切割完毕，共生成%s张小图片。' % num)
    else:
        print('不合法的行列切割参数！')


# 导入图片
src = r'D:\software_practice\get\question(29).jpg'
# src="C：\woman.png"
outfile = r'D:\software_practice\get\question(29).jpg'
img = Image.open(src)
# 让导入的图片像素都变为400*400
(x, y) = img.size  # read image size
x_s = 400  # define standard width
y_s = 400  # calc height based on standard width
out = img.resize((x_s, y_s), Image.ANTIALIAS)  # resize image with high-quality
out.save(outfile)
gameImage = pygame.image.load(src)
gameRect = gameImage.get_rect()
if os.path.isfile(src):
    dstpath = ('')
    if (dstpath == '') or os.path.exists(dstpath):
        row = 3
        col = 3
        if row > 0 and col > 0:
            splitimage(src, row, col, dstpath)
        else:
            print('无效的行列切割参数！')
    else:
        print('图片输出目录%s不存在！' % dstpath)
else:
    print('图片文件%s不存在!' % src)