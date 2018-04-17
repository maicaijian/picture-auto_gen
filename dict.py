# -*- coding: utf-8 i-*-
import os 
#import pygame
import pytesseract
from PIL import Image, ImageFont, ImageDraw,ImageEnhance 
import codecs
dict_2={}
with open("test.txt","r",errors='ignore',encoding='UTF-8') as f:
  j=0
  line_count=0
  for line_1 in f.readlines():
      line_count=line_count+1
      
      if line_count%100==0:
       print("line_count： "+str(line_count))
       #print(dict_2)
      line=""
      line_2=""
      for s in line_1:
       if s!="，" and s!="。" and s!="？" and s!="、" and s!="“" and s!="”" and s!="；":
         line=line+" "+s
         if s!=" ":
          line_2=line_2+s
      j=j+1
      tran=str(line)
      im = Image.new("RGB",(750, 30),(255,255,255))
      dr = ImageDraw.Draw(im)
      font = ImageFont.truetype(os.path.join("fonts", "msyh.ttf"), 15)
      dr.text((5, 5), tran, font=font, fill="#000000")
     # im.save("word_"+str(j)+".png")  
            #亮度增强  
      enh_bri = ImageEnhance.Brightness(im)  
      brightness = 1.5  
      image_brightened = enh_bri.enhance(brightness)  
#image_brightened.show()  
  
#色度增强  
      enh_col = ImageEnhance.Color(im)  
      color = 1.5  
      image_colored = enh_col.enhance(color)  
#image_colored.show()  
      #image_colored.save("r_co.png")
  
#对比度增强  
      enh_con = ImageEnhance.Contrast(image_colored)  
      contrast = 1.5
      image_contrasted = enh_con.enhance(contrast)  
      #image_contrasted.show()
      #image_contrasted.save("word_"+str(j)+".png","PNG") 
     # img=Image.open("word_"+str(j)+".png")
      text_1=pytesseract.image_to_string(image_contrasted,lang='chi_sim')
      t_s=str(text_1)
      l_t=len(str(text_1))
      text_2=""
      l_2=len(line_2)
      for s_2 in t_s:
        if s_2!=" ":
          text_2=text_2+s_2
      try:
       count=0
       for i in range(l_t):
         if i==l_2-1:
          break
         if text_2[i]!=line_2[i] and text_2[i]!=line_2[i-1]:
          #count=count+1
 
          if text_2[i] not in dict_2.keys() and text_2[i]!="" :
             dict_2[text_2[i]]=line_2[i]
          else:
             if str(dict_2[text_2[i]]).contains(str(line_2[i]))==False:
              dict_2[text_2[i]]=str(dict_2[text_2[i]])+" "+str(line_2[i])
         #print(text_2[i]+" "+line_2[i])
        # else:
           #count=0
      except:
        pass
      #print(dict_2)
with open("dict.txt","a+") as f_2:
    print("writing in dict...")
    for key in dict_2.keys():
         f_2.write(key+" "+str(dict_2[key])+"\n")
        
