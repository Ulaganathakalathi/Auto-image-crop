# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 17:03:23 2020

@author: us51114
crop the image
"""
import numpy as np
import cv2

def find_the_diff_corner(img,x_dim,y_dim,str_inp):
    if str_inp=='top':
        start_i=0;stop_i=x_dim;step_i=1
        start_j=0;stop_j=y_dim;step_j=1
        addin=-1
        x_var='i';y_var='j'
    elif str_inp=='bottom':
        start_i=x_dim-1;stop_i=-1;step_i=-1
        start_j=0;stop_j=y_dim-1;step_j=1
        addin=1
        x_var='i';y_var='j'
    elif str_inp=='left':
        start_i=0;stop_i=y_dim-1;step_i=1
        start_j=0;stop_j=x_dim-1;step_j=1
        addin=1
        x_var='j';y_var='i'
    elif str_inp=='right':
        start_i=y_dim-1;stop_i=-1;step_i=-1
        start_j=0;stop_j=x_dim-1;step_j=1
        addin=-1
        x_var='j';y_var='i'
    # print(start_i,":",stop_i,":",step_i)
    # print(start_j,":",stop_j,":",step_j)
    find_val=img[0,0]
    # print("find_val=",type(find_val))
    for i in range(start_i,stop_i,step_i):
        # for j in range(start_j,stop_j,step_j):
            # print(type(img[eval(x_var),eval(y_var)]))
        if x_var=='i':
            cur_val=img[eval(x_var),:]
        else:
            cur_val=img[:,eval(y_var)]
        # cur_val=img[eval(x_var),eval(y_var)]
        comparison = find_val == cur_val 
        equal_arrays = comparison.all() 
        if ~equal_arrays:
            # print('find_val:',find_val,',cur_val:',cur_val)
            index_found=i+addin
            # print('index_found:',index_found,'i:',i)
            return index_found
            
def add_border(img,start_i,stop_i,cont_j,var_axis):
    if var_axis=='x':
        x_var='i';y_var='j'
    else:
        x_var='j';y_var='i'
    set_color=np.array([0,0,255]) #red [blue,green,red]
    for i in range(start_i,stop_i+1,1):
    # for j in range(start_j,stop_j,step_j):
        j=cont_j
        img[eval(x_var),eval(y_var)]=set_color


#import image
# img=cv2.imread('D:\\kalathi\\My_collection\\Python\\Auto_Crop_image\\Picture.jpg')
img=cv2.imread('Input_Image.jpg')
#print(img.shape)
#print(img[0,0])
x=img.shape[0]
# print(x)
y=img.shape[1]
top_loc=find_the_diff_corner(img,x,y,'top')
#print('top_loc=',top_loc)
bot_loc=find_the_diff_corner(img,x,y,'bottom')
left_loc=find_the_diff_corner(img,x,y,'left')
right_loc=find_the_diff_corner(img,x,y,'right')
#print('top_loc=',top_loc,'bot_loc=',bot_loc,'left_loc=',left_loc,'right_loc=',right_loc)

#below to create the red border to image
# ka=add_border(img,left_loc,right_loc,top_loc,'y') #'top line'
# ka=add_border(img,left_loc,right_loc,bot_loc,'y') #'bottom line'
# ka=add_border(img,top_loc,bot_loc,left_loc,'x') #'left line'
# ka=add_border(img,top_loc,bot_loc,right_loc,'x') #'right line'
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
crop_img=img[top_loc:bot_loc+1,left_loc:right_loc+1]
ka=cv2.imwrite('Output_Image.jpg',crop_img)
