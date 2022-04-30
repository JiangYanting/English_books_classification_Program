# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import tkinter as tk
import numpy as np
import farm
from tkinter import filedialog, dialog
from tkinter import *
import transformers
import os
from PIL import Image, ImageTk
import logging
from pathlib import Path
from farm.infer import Inferencer
os.environ["PYTORCH_JIT"] = "0"
import torch
def script_method(fn, _rcb=None):
    return fn


def script(obj, optimize=True, _frames_up=0, _rcb=None):
    return obj


import torch.jit
script_method1 = torch.jit.script_method
script1 = torch.jit.script
torch.jit.script_method = script_method
torch.jit.script = script




global input_string
#第1步，建立窗口window
window = tk.Tk()           #建立窗口window
 
#第2步，给窗口起名称
window.title('English books Classification')      #窗口名称
 
#第3步，设定窗口的大小(长＊高)
window.geometry("600x280") #窗口大小(长＊高)


bm = ImageTk.PhotoImage(file = r"library.png")#file：t图片路径
lab3 = Label(window, image = bm, width =164, height = 111)
lab3.pack(anchor = NW, side = LEFT)     # 显示Label组件
 
#第4步，在图形化界面上设定一个文本框,用于输出预测的label
text1 = tk.Text(window, width=40, height=7, bg='orange', font=('Arial', 12))
text1.pack()
 
output_string = "null" 

#lbl = Label(window, text = "图书类别为...")  #, anchor = "s"
#anchor 规定标签的位置，s为最底端
#lbl.pack(side=LEFT)

#def clicked(output_string):
#    lbl.configure(text = output_string) #使用label的configure方法，动态改变文本标签的内容。
def open_file():
     '''
     打开文件
     :return:
     '''
     global file_path
     global file_text
     file_path = filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser('H:/')))
     print('打开文件：', file_path)
     path_bert = os.getcwd() + "/bert_book_english"
     save_dir = Path(str(path_bert))
     model = Inferencer.load(save_dir, task_type = "text_classification")
     
     if file_path is not None:
          
          file = open(file=file_path, mode='r+', encoding='utf-8')
               
          lst = file.read().split("\n")
          basic = []
          string = ""
          for line in lst:
               line1 = line.strip()
               dic = {"text":line1}
               basic.append(dic)
          result = model.inference_from_dicts(dicts=basic)
          for lst in result:
               results = lst['predictions']
               for dic in results:
                    string = string + dic['context'] + "\t" + dic['label'] + "\t" + str(dic['probability']) + "\n"

          text1.insert('insert', string)

def save_file():
     global file_path
     global file_text
     file_path = filedialog.asksaveasfilename(title=u'保存文件')
     print('保存文件：', file_path)
     file_text = text1.get('1.0', tk.END)
     if file_path is not None:
         with open(file=file_path, mode='a+', encoding='utf-8') as file:
             file.write(file_text)
         text1.delete('1.0', tk.END)
         #Tkinter 文本框控件中第一个字符的位置是 1.0，可以用数字 1.0 或字符串"1.0"来表示。
         #"end"表示它将读取直到文本框的结尾的输入。我们也可以在这里使用 tk.END 代替字符串"end"。
         dialog.Dialog(None, {'title': 'File Modified', 'text': '保存完成', 'bitmap': 'warning', 'default': 0,
                     'strings': ('OK', 'Cancle')})
         print('保存完成')




 
 
#第7步，在图形化界面上设定一个button按钮（#command绑定获取文本框内容的方法）
btnRead=tk.Button(window, height=1, width=25, text="上传英文图书txt文件 每册书一行", command=open_file)   #command绑定获取文本框内容的方法
#第8步，安置按钮
btnRead.pack()      #显示按钮

bt2 = tk.Button(window, text='保存自动分类结果文档', width=25, height=1, command=save_file)
bt2.pack()

email = Label(window, text = "开发者联系方式jiangyanting@mail.bnu.edu.cn", anchor = "s")
#anchor 规定标签的位置，s为最底端
email.pack(side = BOTTOM)

#第9步，
window.mainloop()  #显示窗口
