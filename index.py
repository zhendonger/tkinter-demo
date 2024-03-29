#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter as tk
import tkinter.messagebox
import pickle
from PIL import Image,ImageTk

#窗口
window=tk.Tk()
window.title('欢迎进入学习系统')
# 获取屏幕宽度和高度
scn_w, scn_h = window.maxsize()
# 计算中心坐标
cen_x = (scn_w - 300) / 2
cen_y = (scn_h - 300) / 2
# 设置窗口初始大小和位置
size_xy = '%dx%d+%d+%d' % (500, 310, cen_x, cen_y)

window.geometry(size_xy)  #设置窗口坐标   
window.wm_attributes('-topmost',1)# 窗口置顶

#画布放置图片
canvas=tk.Canvas(window,height=300,width=500)
im=Image.open("./img/1.jpg")
imagefile=ImageTk.PhotoImage(im)
# imagefile=tk.PhotoImage(file='71.gif')
image=canvas.create_image(0,0,anchor='nw',image=imagefile)
canvas.pack(side='top')
#标签 用户名密码
tk.Label(window,text='用户名:').place(x=100,y=150)
tk.Label(window,text='密码:').place(x=100,y=190)
#用户名输入框
var_usr_name=tk.StringVar()
entry_usr_name=tk.Entry(window,textvariable=var_usr_name)
entry_usr_name.place(x=160,y=150)
#密码输入框
var_usr_pwd=tk.StringVar()
entry_usr_pwd=tk.Entry(window,textvariable=var_usr_pwd,show='*')
entry_usr_pwd.place(x=160,y=190)
 
#登录函数
def usr_log_in():
    #输入框获取用户名密码
    usr_name=var_usr_name.get()
    usr_pwd=var_usr_pwd.get()
    #从本地字典获取用户信息，如果没有则新建本地数据库
    try:
        with open('usr_info.pickle','rb') as usr_file:
            usrs_info=pickle.load(usr_file)
    except FileNotFoundError:
        with open('usr_info.pickle','wb') as usr_file:
            usrs_info={'admin':'admin'}
            pickle.dump(usrs_info,usr_file)
    #判断用户名和密码是否匹配
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            # tk.messagebox.showinfo(title='welcome',
            #                        message='欢迎您：'+usr_name)
            show_info()
        else:
            tk.messagebox.showerror(message='密码错误')
    #用户名密码不能为空
    elif usr_name=='' or usr_pwd=='' :
        tk.messagebox.showerror(message='用户名或密码为空')
    #不在数据库中弹出是否注册的框
    else:
        is_signup=tk.messagebox.askyesno('欢迎','您还没有注册，是否现在注册')
        if is_signup:
            usr_sign_up()
#登陆成功展示函数
def show_info():
    #新建登陆成功界面
    window.withdraw()
    window_info_up=tk.Toplevel(window)
    size_xy = '%dx%d+%d+%d' % (500, 658, cen_x, cen_y)
    window_info_up.geometry(size_xy)  #设置窗口坐标   
    window_info_up.wm_attributes('-topmost',1)# 窗口置顶
    window_info_up.title('欢迎进入魔幻世界')
    #画布放置图片
    canvas=tk.Canvas(window_info_up,height=987,width=658)
    im=Image.open("./img/3.jpg")
    imagefile=ImageTk.PhotoImage(im)
    # imagefile=tk.PhotoImage(file='71.gif')
    image1=canvas.create_image(0,0,anchor='nw',image=imagefile)
    canvas.pack(side='top')
    tk.Label(window_info_up,text='No matter how far you may fly, never forget where you come from.').place(x=25,y=100)
    tk.Label(window_info_up,text='No matter how far you may fly, never forget where you come from.').place(x=25,y=140)
    tk.Label(window_info_up,text='No matter how far you may fly, never forget where you come from.').place(x=25,y=180)

    bt_logquit=tk.Button(window_info_up,text='退出',command=usr_sign_quit)
    bt_logquit.place(x=430,y=10)
    def callback():
        window.destroy()
    window_info_up.protocol("WM_DELETE_WINDOW", callback)
    window_info_up.mainloop()
    
#注册函数
def usr_sign_up():
    #确认注册时的相应函数
    def signtowcg():
        #获取输入框内的内容
        nn=new_name.get()
        np=new_pwd.get()
        npf=new_pwd_confirm.get()
 
        #本地加载已有用户信息,如果没有则已有用户信息为空
        try:
            with open('usr_info.pickle','rb') as usr_file:
                exist_usr_info=pickle.load(usr_file)
        except FileNotFoundError:
            exist_usr_info={}           
            
        #检查用户名存在、密码为空、密码前后不一致
        if nn in exist_usr_info:
            tk.messagebox.showerror('错误','用户名已存在')
        elif np =='' or nn=='':
            tk.messagebox.showerror('错误','用户名或密码为空')
        elif np !=npf:
            tk.messagebox.showerror('错误','密码前后不一致')
        #注册信息没有问题则将用户名密码写入数据库
        else:
            exist_usr_info[nn]=np
            with open('usr_info.pickle','wb') as usr_file:
                pickle.dump(exist_usr_info,usr_file)
            tk.messagebox.showinfo('欢迎','注册成功')
            #注册成功关闭注册框
            window_sign_up.destroy()
    #新建注册界面
    window_sign_up=tk.Toplevel(window)
    window_sign_up.geometry(size_xy)  #设置窗口坐标   
    window_sign_up.wm_attributes('-topmost',1)# 窗口置顶
    window_sign_up.title('注册界面')
    #画布放置图片
    canvas=tk.Canvas(window_sign_up,height=300,width=500)
    im=Image.open("./img/2.png")
    imagefile=ImageTk.PhotoImage(im)
    # imagefile=tk.PhotoImage(file='71.gif')
    image1=canvas.create_image(0,0,anchor='nw',image=imagefile)
    canvas.pack(side='top')
    #用户名变量及标签、输入框
    new_name=tk.StringVar()
    tk.Label(window_sign_up,text='用户名：').place(x=100,y=100)
    tk.Entry(window_sign_up,textvariable=new_name).place(x=240,y=100)
    #密码变量及标签、输入框
    new_pwd=tk.StringVar()
    tk.Label(window_sign_up,text='请输入密码：').place(x=100,y=140)
    tk.Entry(window_sign_up,textvariable=new_pwd,show='*').place(x=240,y=140)    
    #重复密码变量及标签、输入框
    new_pwd_confirm=tk.StringVar()
    tk.Label(window_sign_up,text='请再次输入密码：').place(x=100,y=180)
    tk.Entry(window_sign_up,textvariable=new_pwd_confirm,show='*').place(x=240,y=180)    
    #确认注册按钮及位置
    bt_confirm_sign_up=tk.Button(window_sign_up,text='确认注册',
                                 command=signtowcg)
    bt_confirm_sign_up.place(x=240,y=220)
    window_sign_up.mainloop()
#退出的函数
def usr_sign_quit():
    window.destroy()
#登录 注册按钮
bt_login=tk.Button(window,text='登录',command=usr_log_in)
bt_login.place(x=140,y=230)
bt_logup=tk.Button(window,text='注册',command=usr_sign_up)
bt_logup.place(x=210,y=230)
bt_logquit=tk.Button(window,text='退出',command=usr_sign_quit)
bt_logquit.place(x=280,y=230)

#主循环
window.mainloop()