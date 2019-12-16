#!/usr/bin/env python
# encoding: utf-8
# @Time : 2019-12-13 15:59

__author__ = 'Ted'
# Version for Windows

import tkinter
from tkinter import font,messagebox
import time
import threading
import random
import pandas as pd
from PIL import ImageTk, Image
import copy
import sys


class LuckyDraw:
    def __init__(self,data):
        # 准备好界面
        self.root = tkinter.Tk()
        self.root.title("2019 圣诞大抽奖")
        self.root.geometry('1360x700+0+0')  # 定义界面大小
        self.root.resizable(False, False)

        # 添加背景图片
        self.canvas = tkinter.Canvas(self.root,
                                width=1360,  # 指定Canvas组件的宽度
                                height=700,  # 指定Canvas组件的高度
                                bg='white')  # 指定Canvas组件的背景色
        self.image = Image.open("static/background.png")
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(680, 350, image=self.im)  # 使用create_image将图片添加到Canvas组件中
        self.canvas.pack()

        reset_img = Image.open("static/reset.png")
        res = ImageTk.PhotoImage(reset_img)
        self.label_reset = tkinter.Label(self.root, image=res)
        self.label_reset.place(x=180, y=550, width=140, height=36)
        self.label_reset.bind("<Button-1>",self.reset)

        nose_img = Image.open("static/nose.png")
        nose = ImageTk.PhotoImage(nose_img)
        self.label_start = tkinter.Label(self.root, image=nose)
        self.label_start.place(x=660, y=370, width=60, height=42)
        self.label_start.bind("<Button-1>",self.newtask)

        img_03 = Image.open("static/003.png")
        label_03 = ImageTk.PhotoImage(img_03)
        self.third = tkinter.Label(self.root, image=label_03)
        self.third.place(x=926, y=533, width=80, height=54)
        self.third.bind("<Button-1>",self.set_third)

        img_02 = Image.open("static/002.png")
        label_02 = ImageTk.PhotoImage(img_02)
        self.second = tkinter.Label(self.root, image=label_02)
        self.second.place(x=1218, y=362, width=80, height=55)
        self.second.bind("<Button-1>",self.set_second)

        img_01 = Image.open("static/001.png")
        label_01 = ImageTk.PhotoImage(img_01)
        self.first = tkinter.Label(self.root, image=label_01)
        self.first.place(x=1108, y=35, width=80, height=54)
        self.first.bind("<Button-1>",self.set_first)

        # 添加键盘控制
        self.root.bind("1", self.set_first)
        self.root.bind("2", self.set_second)
        self.root.bind("3", self.set_third)
        self.root.bind("<space>", self.newtask)
        self.root.bind("<Escape>", self.close)


        # 声明一个是否按下开始的变量
        self.isloop = False
        self.newloop = False

        self.original = copy.deepcopy(data)
        self.data = data

        #调用设置界面的方法
        self.setwindow()
        self.root.mainloop()

    #界面布局方法
    def setwindow(self):

        # self.btn_reset = tkinter.Button(self.root, text = '重启', command = self.reset ,bg='gold')
        # self.btn_reset.place(x=180, y=550, width=100, height=50)

        #开始停止按钮
        # self.btn_start = tkinter.Button(self.root, text = '开始/停止', command = self.newtask,bg='gold')
        # self.btn_start.place(x=660, y=370, width=60, height=40)


        # self.third = tkinter.Button(self.root, text = '三等奖', command = self.set_third,bg='gold')
        # self.third.place(x=920, y=530, width=80, height=50)
        # self.second = tkinter.Button(self.root, text = '二等奖', command = self.set_second,bg='gold')
        # self.second.place(x=960, y=380, width=80, height=50)
        # self.first = tkinter.Button(self.root, text = '一等奖', command = self.set_first,bg='gold')
        # self.first.place(x=1070, y=180, width=80, height=50)

        displayfont = font.Font(size=22)
        self.btn1 = tkinter.Button(self.root, text='', bg='lightyellow',font=displayfont)
        # self.btn1.config(font=("Courier", 30))
        self.btn1.place(x=640, y=500, width=100, height=70)

        self.source = tkinter.Text(self.root,bg="navajowhite",fg="dimgray")
        self.source.place(x=100, y=250, width=300, height=290)
        self.source.insert(tkinter.END,("、").join(self.data))

        myFont = font.Font(size=20)
        self.target_3 = tkinter.Listbox(self.root,height=5,font=myFont,bg="burlywood",bd=1,fg="saddlebrown")
        self.target_3.place(x=1020, y=455, width=110, height=145)

        self.target_3_sub = tkinter.Listbox(self.root,height=5,font=myFont,bg="burlywood",bd=1,fg="saddlebrown")
        self.target_3_sub.place(x=1170, y=455, width=110, height=145)

        self.target_2 = tkinter.Listbox(self.root,height=5,font=myFont,bg="gainsboro",bd=1,fg="dimgrey")
        self.target_2.place(x=1095, y=295,  width=110, height=145)

        self.target_1 = tkinter.Listbox(self.root,height=5,font=myFont,bg="lemonchiffon",bd=1,fg="olive")
        self.target_1.place(x=1095, y=135, width=110, height=145)

        self.target = self.target_3




    def rounds(self):
        # 判断是否开始循环
        if self.isloop == True:
            return

        # 初始化计数 变量
        i = 0
        # 死循环
        while True:
            if self.newloop == True:
                self.newloop = False
                if self.target.size()>=5:
                    if self.target==self.target_3:
                        self.target=self.target_3_sub
                    else:
                        self.btn1['text'] = "Bye～"
                        tkinter.messagebox.showinfo('提示', "本轮抽奖结束!")
                        return
                self.target.insert(tkinter.END, r.center(5," "))
                self.data.remove(temp)
                self.source.delete(1.0,'end')
                self.source.insert(tkinter.END, ("、").join(self.data))
                return

            # 延时操作
            time.sleep(0.1)
            temp = random.choice(self.data)
            if len(temp) == 2:
                r = temp[0]+f"{chr(12288)}"+temp[1]
            else:
                r = temp
            self.btn1['text'] = r



    # 建立一个新线程的函数
    def newtask(self,event):
        if self.isloop == False:
            # 建立线程
            t = threading.Thread(target = self.rounds)
            # 开启线程运行
            t.start()
            # 设置循环开始标志ask(self):nknewtas
            self.isloop = True
        elif self.isloop == True:
            self.isloop = False
            self.newloop = True

    def set_third(self,event):
        if self.target_3.size()>=5:
            if self.target_3_sub.size()>=5:
                tkinter.messagebox.showinfo('提示',"三等奖（10位）已产生！")
            else:
                self.target = self.target_3_sub
        else:
            self.target = self.target_3

    def set_second(self,event):
        if self.target_2.size()>=5:
            tkinter.messagebox.showinfo('提示',"二等奖（5位）已产生！")
        else:
            self.target = self.target_2

    def set_first(self,event):
        if self.target_1.size()>=5:
            tkinter.messagebox.showinfo('提示',"一等奖（5位）已产生！")
        else:
            self.target = self.target_1

    def reset(self,event):
        self.data = copy.deepcopy(self.original)
        self.setwindow()

    def close(self,event):
        self.root.withdraw()
        sys.exit()




if __name__ == '__main__':

    data = pd.read_excel("demo.xlsx")
    name_list=[item for item in data['名字']]
    print(name_list)

    c = LuckyDraw(name_list)