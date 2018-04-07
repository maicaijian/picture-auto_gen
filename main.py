# -*- coding: utf-8 i-*-
import os 
#import pygame
import pytesseract
from PIL import Image, ImageFont, ImageDraw
import codecs
list3=[]
final_str=u""
start,end = (0x4E00, 0x4E50)
chinese_dir = 'chinese'
if not os.path.exists(chinese_dir): 
 os.mkdir(chinese_dir) 
  
#pygame.init()
tran=""
i=0 
list1=[]
f_dict={}
start=int(start)
mid=int(start)
end=int(end)-10
mid_1=start+10
print(end)
#with codecs.open("chinese.txt", "a+", encoding="utf-8") as f:
#with codecs.open("final_r.txt", "w", encoding="utf-8") as f:
for mid in range(start,mid_1):
 mid=mid+1
 print(mid)
 for codepoint in range(mid,end): 
  word = chr(codepoint) 
  list1.append(word)
  im = Image.new("RGB", (300, 50), (255, 255, 255))
  dr = ImageDraw.Draw(im)
  font = ImageFont.truetype(os.path.join("fonts", "/home/maicaijian/msyh.ttf"), 14)
#rtext = font.render(word, True, (0, 0, 0), (255, 255, 255))
# list1.append(word)
# print(list1)
  i=i+1
  tran=tran+word
  if i==10:
      i=0
     # list1=list(tran)    
      dr.text((10, 5), tran, font=font, fill="#000000")
     # print(list1)
     #print(len(list1))
      print(tran)
    # list1=[]
    # im.show()
      im.save("line.jpg")
      img=Image.open('line.jpg')
      text2=pytesseract.image_to_string(img,lang='chi_sim')
      text_z=u"%s"%text2
      print(text_z)
      list2=list(text_z)
      #list1=repr(list1).decode('unicode-escape')
     # print(list1)
      if len(list2)==10:
         for i in reversed(range(0,9)):
            if list1[i]==list2[i]:
                       # print((list1[i],list2[i]))
                        list1.remove(list1[i])
                        list2.remove(list2[i])
            else :
                        str1="hello" # list1[i]=str(list1[i]).decode('string-escape')
                       # list3.append((list2[i],list1[i]))
                        #list2[i]=repr(list2[i]).decode('unicode-escape')
        # list1=repr(list1).decode('unicode-escape').encode('utf-8')
        # list2=repr(list2).decode('unicode-escape').encode('utf-8')
     # print(list1)
         a=len(list1)
         if a!=0:
          for k in range(0,len(list1)-1):
           try:  

             if f_dict.has_key(list2[k]):
                        if str(list1[k]) in str(f_dict[list2[k]]):
                             f_dict[list2[k]]=str(f_dict[list2[k]])
                        else:
                             
                             f_dict[list2[k]]=str(f_dict[list2[k]])+str(list1[k])
             else:
                        f_dict[list2[k]]=str(list1[k])
           except:
             print("sorry ,sorry")
       #  print(f_dict.values())
    
      list1=[]
      list2=[]
      tran=""
f1=open("f_dict.txt","a+")
f1.write(str(f_dict))
f1.close
#font = pygame.font.Font("msyh.ttc", 22)#微软雅黑的字体文件msyh
# rtext = font.render(word, True, (0, 0, 0), (255, 255, 255)) # pygame.image.save(rtext, os.path.join(chinese_dir,word+".png"))  
