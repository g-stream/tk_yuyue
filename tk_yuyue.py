# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 20:13:22 2015

@author: yinly
"""
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *

import datetime


from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter


import os
from io import BytesIO
import requests

from lxml import etree
_version = 'Bate 0.1'
class Application(Frame):
    def __init__(self, master=None):
        self.message_queue = [['','black'] for i in range(8)]        
        Frame.__init__(self, master = None)
        self.pack()
        


        self.fresh = Button(self,text='刷新',command = fresh_by_fresh)
        self.get   = Button(self, text="抢场",command = yuyue)
        self.fresh.grid(row=12,column=6,columnspan = 3, rowspan = 2)
        self.get.grid(row=12,column=9,columnspan = 3, rowspan = 2)
        
        self.message_label_list = [Label(self,text='',foreground = 'green') for i in range(8)]
        for i in range(8):
            self.message_label_list[i].grid(row=3+i,column=6,columnspan = 6)    
        
        
        self.date_button0 = Button(self,command = self.label_fresh0, text = (datetime.datetime.today()+datetime.timedelta(days=0)).strftime("%Y-%m-%d"))
        self.date_button1 = Button(self,command = self.label_fresh1, text = (datetime.datetime.today()+datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
        self.date_button2 = Button(self,command = self.label_fresh2, text = (datetime.datetime.today()+datetime.timedelta(days=2)).strftime("%Y-%m-%d"))
        self.date_button3 = Button(self,command = self.label_fresh3, text = (datetime.datetime.today()+datetime.timedelta(days=3)).strftime("%Y-%m-%d"))
        self.date_button0.grid(row = 0, column = 0,columnspan = 3)
        self.date_button1.grid(row = 0, column = 3,columnspan = 3)
        self.date_button2.grid(row = 0, column = 6,columnspan = 3)
        self.date_button3.grid(row = 0, column = 9,columnspan = 3)
        self.date_value = datetime.datetime.today().strftime("%Y-%m-%d")
        
        self.label_list = [Label(self,text='-/-') for i in range(12)]
        for i in range(12):
            self.label_list[i].grid(row=2+i,column=4,columnspan = 2)
        self.label_state_list = [[['-/-','black'] for i in range(12)] for k in range(4)]
        self.label_state_now = 0
        
        self.radiobutton_date_list = ['09:00-10:00','10:00-11:00','11:00-12:00','12:00-13:00','13:00-14:00','14:00-15:00','15:00-16:00','16:00-17:00','17:00-18:00','18:00-19:00','19:00-20:00','20:00-21:00']
        self.radiobutton_list = [Radiobutton(self, text = i, variable = var, value = i) for i in self.radiobutton_date_list]
        for i in range(12):
            self.radiobutton_list[i].grid(row=2+i, column=0,columnspan=4)

    def message_processing(self,message,color = 'black'):
        self.message_queue.insert(0,[message,color])
        for i in range(8):
            self.message_label_list[i].config(text = self.message_queue[i][0],foreground = self.message_queue[i][1])
        self.message_queue.pop()
    
    def label_fresh0(self):
        for i in range(12):
            self.label_list[i].config(text = self.label_state_list[0][i][0],foreground = self.label_state_list[0][i][1])
        self.date_value = self.date_button0['text']
        self.message_processing("选择了时期： "  + self.date_button0['text'])
        self.label_state_now = 0
        
    def label_fresh1(self):
        for i in range(12):
            self.label_list[i].config(text = self.label_state_list[1][i][0],foreground = self.label_state_list[1][i][1])
        self.date_value = self.date_button1['text']
        self.message_processing("选择了时期： "  + self.date_value)
        self.label_state_now = 1
    def label_fresh2(self):
        for i in range(12):
            self.label_list[i].config(text = self.label_state_list[2][i][0],foreground = self.label_state_list[2][i][1])
        self.date_value = self.date_button2['text']
        self.message_processing("选择了时期： "  + self.date_button2['text'])
        self.label_state_now = 2
        
    def label_fresh3(self):
        for i in range(12):
            self.label_list[i].config(text = self.label_state_list[3][i][0],foreground = self.label_state_list[3][i][1])
        self.date_value = self.date_button3['text']
        self.message_processing("选择了时期： "  + self.date_button3['text'])
        self.label_state_now = 3





def processing_im(im):
    t = im.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(t)
    t = enhancer.enhance(8)
    t = t.convert('L')
    return t.point(lambda i:i>70 and 225)
def flaten_im(im):
    list = []
    for i in range(20):
        list.extend([im.getpixel((k,i)) for k in range(13)])
    return list
    
#pic_list=os.listdir("/home/yinly/data/temp/")
#absolute_path = [os.path.join("/home/yinly/data/temp",i) for i in pic_list]
#sample_data = {str(i):flaten_im(processing_im(Image.open(os.path.join("/home/yinly/data/temp",str(i))))) for i in range(10)}
sample_data = {'2': [225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225], '3': [225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225], '5': [225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225], '9': [225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225], '7': [225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225], '8': [225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225], '4': [225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225], '0': [225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225], '1': [225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225], '6': [225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225]}



def im_crop_and_processing_and_flaten(im):
    return [flaten_im(processing_im(im.crop(((4+13*k),0,(17+13*k),20)))) for k in range(4)]
def score_of_list(list1,list2):
    return sum([int(list1[i]==list2[i]) for i in range(len(list1))])

def max_value(test,sample):
    m = 0    
    for k,v in sample.items():
        if score_of_list(v,test)>m:
            out = k
            m =score_of_list(v,test)
    return out
def value(im):
    a = [max_value(i,sample_data) for i in im_crop_and_processing_and_flaten(im)]
    b = ''
    for i in a:
        b = b+i
    return b


s = requests.session()

username  = '213132436'
passwords = '010100cyl'
date = ''
time = ''
phone_number = '11111111111'

main_url         = 'http://yuyue.seu.edu.cn/eduplus/order/initOrderIndex.do?sclId=1'

login_im_url     = "http://ids1.seu.edu.cn/amserver/verify/image.jsp"
validatecode = None

login_check_url  = "http://ids1.seu.edu.cn/amserver/verify/check.jsp"
login_check_data = {'inputCode':validatecode}

login_url        = "http://ids1.seu.edu.cn/amserver/UI/Login"
login_data = {'IDButton'    :'Submit',
              'IDToken0'    :'',
              'IDToken1'    :username,
              'IDToken2'    :passwords,
              'goto'        :main_url,
              'gx_charset'  :'gb2312'}             



yuyue_im_url     = 'http://yuyue.seu.edu.cn/eduplus/control/validateimage'
yuyue_judge_url  = 'http://yuyue.seu.edu.cn/eduplus/order/order/order/judgeUseUser.do?sclId=1'
yuyue_judge_data ={'allowHalf'   :'2',
                   'ids'         :'13486,',
                   'itemId'      :'10',
                   'useTime'     :date + ' ' + time,
                   'validateCode':validatecode}
yuyue_insert_url  = 'http://yuyue.seu.edu.cn/eduplus/order/order/order/insertOredr.do?sclId=1'
yuyue_insert_data = {'orderVO.itemId' :'10',
                     'orderVO.phone'  :phone_number,
                     'orderVO.remark' :'',
                     'orderVO.useMode':'2',
                     'orderVO.useTime':date + ' ' + time,
                     'useUserIds'     :'13486',
                     'validateCode'   :validatecode}
fresh_url         = 'http://yuyue.seu.edu.cn/eduplus/order/order/getOrderInfo.do?sclId=1'
def validatecode_get(url):
    global s
    im_get = s.get(url)
    im = Image.open(BytesIO(im_get.content))
    return value(im)


login_state = 0
'''
def login_test():
    if len(re.findall('羽毛球',s.get(main_url).text)):
'''        
def login():
    app.message_processing('正在登录...')
    validatecode = validatecode_get(login_im_url)
    s.post(login_check_url,data = login_check_data)
    app.message_processing('验证码获取并通过！')
    s.post(login_url,data = login_data)
    login_state = 1
    
def yuyue():
    if login_state:
        pass
    else:
        login()
    date_time = app.date_value + ' ' + var.get()
    yuyue_judge_data['useTime'] = date_time
    yuyue_insert_data['orderVO.useTime'] = date_time
    app.message_processing('正在抢场...')
    validatecode = validatecode_get(yuyue_im_url)
    s.post(yuyue_judge_url,data = yuyue_judge_data)
    app.message_processing('验证码获取并通过！')
    s.post(yuyue_insert_url,data = yuyue_insert_data)

    app.message_processing('完成,检验是否成功中...')
    

root = Tk()
root.title('抢场小助手 '+_version)
menu_main   = Menu(root)
menu_shezhi = Menu(menu_main)
menu_about  = Menu(menu_main)
root.config(menu = menu_main)


menu_main.add_cascade(label = '设置', menu = menu_shezhi)
menu_shezhi.add_checkbutton(label = '自动刷场')

def show_info():
    showinfo("抢场程序","Created by: yinly\n天天打球身体好")
menu_main.add_cascade(label = '关于', menu = menu_about)
menu_about.add_command(label = '关于',command = show_info)



fresh_data_list = [[{'dayInfo'   :(datetime.datetime.today()+datetime.timedelta(days=i)).strftime("%Y-%m-%d"),
                   'itemId'    :'10',
                   'pageNumber':str(k)} for k in [1,2]] for i in range(3)]



def fresh_html_processing(html):
    tree = etree.fromstring(html,etree.HTMLParser())
    item = tree.xpath("//div[@class='time-item']")
    process1 = [[i.xpath("./em[@class='time']/text()")[0],i.xpath("./em[@class='time2']")[0].xpath('string(.)')] for i in item]
  
    d = {}    
    for i in process1:
        re1 = re.search("\d{2}:\d{2}-\d{2}:\d{2}",i[0])
        re2 = re.search('(\d).*(\d)',i[1],re.S)
        d[re1.group(0)]=(str(int(re2.group(2))-int(re2.group(1)))+'/'+re2.group(2))
    return d

def label_text():
    global s
    if login_state:
        pass
    else:
        login()
    fresh_html_list = [[s.post(fresh_url,i).text for i in k] for k in fresh_data_list]

    order = ['09:00-10:00','10:00-11:00','11:00-12:00','12:00-13:00','13:00-14:00','14:00-15:00','15:00-16:00','16:00-17:00','17:00-18:00','18:00-19:00','19:00-20:00','20:00-21:00']    
    out = []    
    for i in fresh_html_list:
        d1 = fresh_html_processing(i[0])
        d2 = fresh_html_processing(i[1])
        d = {}
        for k,v in (list(d1.items()) + list(d2.items())):
            d[k] = v
        if len(d) == 12:
            out.append([d[i] for i in order])
        else:
            app.message_processing('获取数据失败',color = 'red')
    return out

def fresh_by_fresh():
    global s
    if login_state:
        pass
    else:
        login()    
    got_data = label_text()
    for i in range(3):
        for k in range(12):
            app.label_state_list[i][k][0]=got_data[i][k]
            if got_data[i][k][0] != '0':
                app.label_state_list[i][k][1]='black'
            else:
                app.label_state_list[i][k][1]='red'
    for i in range(12):
        app.label_list[i].config(text = app.label_state_list[app.label_state_now][i][0],foreground = app.label_state_list[app.label_state_now][i][1])
    app.message_processing("完成刷新")


var = StringVar()


app = Application(master=root)
app.mainloop()
