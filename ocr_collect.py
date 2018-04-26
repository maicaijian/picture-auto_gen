# -*- coding: UTF-8 -*-
import cv2
import sys
import matplotlib.pyplot as plt
import numpy as np
import pytesseract
from PIL import Image
import os
from Tesserast_ocr import tesseractChinese
from Tesserast_ocr import tesseractSex
from Tesserast_ocr import tesseractNationality
from Tesserast_ocr import tesseractDate
from Tesserast_ocr import tesseractID
from platenumber import preprocess
from platenumber import findPlateNumberRegion
from platenumber import detect
from IDcard import box_get
from IDcard import text_get

if __name__=="__main__":
  path=sys.argv[1]
  tpye=sys.argv[2]
  if tpye=="doc":

    
    im = Image.open(path)
#img=Image.open(path)
    text_1=pytesseract.image_to_string(im,lang='chi_sim')
    print(text_1)

     
  if tpye=="ID":
    #paths=['test1.png']
    #for path in paths:
        #Index=paths.index(path)
        img = cv2.imread(path)
        height, width = img.shape[:2]
        imgWidth = width
        imgHeight = height
        img = cv2.resize(img, (imgWidth, imgHeight))
        Name, Sex, Nationality, Birth_year, Birth_month, Birth_day, Address, ID_number=box_get(img,imgHeight,imgWidth,Index)
        #show the img
        f, axarr = plt.subplots(3, 3)
        axarr[0, 0].set_title('origin img')
        axarr[0, 1].set_title('Name')
        axarr[0, 2].set_title('Sex')
        axarr[1, 0].set_title('Nationality')
        axarr[1, 1].set_title('Birth_year')
        axarr[1, 2].set_title('Birth_month')
        axarr[2, 0].set_title('Birth_day')
        axarr[2, 1].set_title('Address')
        axarr[2, 2].set_title('ID_number')
        axarr[0, 0].imshow(img)
        axarr[0, 1].imshow(Name)
        axarr[0, 2].imshow(Sex)
        axarr[1, 0].imshow(Nationality)
        axarr[1, 1].imshow(Birth_year)
        axarr[1, 2].imshow(Birth_month)
        axarr[2, 0].imshow(Birth_day)
        axarr[2, 1].imshow(Address)
        axarr[2, 2].imshow(ID_number)
        plt.show()
        Information=text_get(Name, Sex, Nationality, Birth_year, Birth_month, Birth_day, Address, ID_number)
        print('the information is as following\n',
              '-------------------------------\n',
              'the name is {} \n'.format(Information[0]),
              'the sex is {} \n'.format(Information[1]),
              'the Nationality is {} \n'.format(Information[2]),
              'the birth is {} 年 {} 月 {} 日 \n'.format(Information[3],Information[4],Information[5]),
              'the Address is {} \n'.format(Information[6]),
              'the ID_number is {} \n'.format(Information[7]),
              '-------------------------------\n\n')
if tpye=="car":
  #imagePath = '10.jpg'
	img = cv2.imread(path)
	detect(img)
  re_img=image.open("c://number_plate.png")
  text_1=pytesseract.image_to_string(re_img,lang='chi_sim')
  print(text_1)
if type=="title":
    im = Image.open(path)
    img_size = im.size
    region = im.crop((0, 0, img_size[0], 100))
    #region.show()
#img=Image.open(path)
    text_1=pytesseract.image_to_string(region,lang='chi_sim')
    print(text_1)
  
if tpye=="bankcard":
else:
  print("please input correct tpye")
    
