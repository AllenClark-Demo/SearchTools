# -*-coding:utf-8-*-
import re
import tkinter as tk
import tkinter.messagebox as msgbox
import webbrowser
 
"""
vip视频解析类
"""
 
 
class VideoMenu():
    # 构造函数，用于初始化全部变量
    def __init__(self, width=650, height=400, background='grey'):
        self.w = width
        self.h = height
        self.bg = background
        self.title = '资源搜索器                   By:S K'
        self.main = tk.Tk(className=self.title)
        #self.main.iconbitmap('resources/s.ico')
        self.url = tk.StringVar()
        self.v = tk.IntVar()
        self.v.set(1)
        self.filename=tk.StringVar()
        self.x = tk.IntVar()
        self.x.set(1)
        
        frame1 = tk.Frame(self.main)
        frame2 = tk.Frame(self.main)
        

        menu = tk.Menu(self.main)
        self.main.config(menu=menu)
        menu1 = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label='友情链接（L）', menu=menu1)
        menu1.add_command(label='B站', command=lambda: webbrowser.open('https://www.bilibili.com/'))
        menu1.add_command(label='A站', command=lambda: webbrowser.open('https://www.acfun.cn/'))
        menu1.add_command(label='优酷', command=lambda: webbrowser.open('https://www.youku.com/'))
        menu1.add_command(label='爱奇艺', command=lambda: webbrowser.open('http://www.iqiyi.com/'))
        menu1.add_command(label='腾讯视频', command=lambda: webbrowser.open('https://v.qq.com/'))
        menu1.add_command(label='搜狐视频', command=lambda: webbrowser.open('https://tv.sohu.com/'))
        menu1.add_command(label='乐视网', command=lambda: webbrowser.open('http://www.le.com/zt/letvtv/'))
        menu1.add_command(label='电影天堂', command=lambda: webbrowser.open('https://www.dytt8.net/'))
        menu1.add_command(label='YouTobe', command=lambda: webbrowser.open('http://www.youtube.com/'))
        menu1.add_command(label='退出', command=lambda: self.main.quit())



        menu2 = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label='帮助（H）', menu=menu2)
        menu2.add_command(label='使用说明',
            command=lambda:msgbox.showinfo(title='帮助',
                message=
                '1.将VIP付费视频的网址复制到视频地址输入框中，点击开始播放即可播放，如果打不开可以多换几个接口尝试。2.百度网盘搜索框可以搜索百度网盘资源，可以在三个接口中切换。3.此软件仅用于学习交流。（2019.8.9）'))
 



        group = tk.Label(frame1, text='请选择视频解析接口：',font=('Arial',12),padx=10, pady=10)
        group2 = tk.Label(frame1,text='请选择网盘搜索接口：',font=('Arial',12),padx=10, pady=10)

        tb1=tk.Radiobutton(frame1,text='通用接口1',
            variable=self.v,value=1,width=10,height=1)
        tb2=tk.Radiobutton(frame1,text='通用接口2',
            variable=self.v,value=2,width=10,height=1)
        tb3=tk.Radiobutton(frame1,text='通用接口3',
            variable=self.v,value=3,width=10,height=1)
        tb4=tk.Radiobutton(frame1,text='通用接口4',
            variable=self.v,value=4,width=10,height=1)
        tb5=tk.Radiobutton(frame1,text='通用接口5',
            variable=self.v,value=5,width=10,height=1)
        tb6=tk.Radiobutton(frame1,text='通用接口6',
            variable=self.v,value=6,width=10,height=1)
        tb7=tk.Radiobutton(frame1,text='通用接口7',
            variable=self.v,value=7,width=10,height=1)
        tb8=tk.Radiobutton(frame1,text='通用接口8',
            variable=self.v,value=8,width=10,height=1)
        tb9=tk.Radiobutton(frame1,text='通用接口9',
            variable=self.v,value=9,width=10,height=1)
        tb10=tk.Radiobutton(frame1,text='通用接口10',
            variable=self.v,value=10,width=10,height=1)
        tb11=tk.Radiobutton(frame1,text='通用接口11',
            variable=self.v,value=11,width=10,height=1)
        tb12=tk.Radiobutton(frame1,text='通用接口12',
            variable=self.v,value=12,width=10,height=1)
        tb13=tk.Radiobutton(frame1,text='通用接口13',
            variable=self.v,value=13,width=10,height=1)
        tb14=tk.Radiobutton(frame1,text='通用接口14',
            variable=self.v,value=14,width=10,height=1)
        tb15=tk.Radiobutton(frame1,text='通用接口15',
            variable=self.v,value=15,width=10,height=1)
        tb16=tk.Radiobutton(frame1,text='通用接口16',
            variable=self.v,value=16,width=10,height=1)

        tb17=tk.Radiobutton(frame1,text='腾讯视频接口',
            variable=self.v,value=17,width=10,height=1)
        tb18=tk.Radiobutton(frame1,text='爱奇艺接口1',
            variable=self.v,value=18,width=10,height=1)
        tb19=tk.Radiobutton(frame1,text='爱奇艺接口2',
            variable=self.v,value=19,width=10,height=1)
        tb20=tk.Radiobutton(frame1,text='爱奇艺接口3',
            variable=self.v,value=20,width=10,height=1)
        tb21=tk.Radiobutton(frame1,text='芒果TV接口',
            variable=self.v,value=21,width=10,height=1)
        tb22=tk.Radiobutton(frame1,text='优酷超清接口',
            variable=self.v,value=22,width=10,height=1)
        tb23=tk.Radiobutton(frame1,text='搜狐视频接口',
            variable=self.v,value=23,width=10,height=1)
        tb24=tk.Radiobutton(frame1,text='乐视视频接口',
            variable=self.v,value=24,width=10,height=1)


        tb25=tk.Radiobutton(frame1,text='网盘接口1',
            variable=self.x,value=1,width=10,height=1)
        tb26=tk.Radiobutton(frame1,text='网盘接口2',
            variable=self.x,value=2,width=10,height=1)
        tb27=tk.Radiobutton(frame1,text='网盘接口3',
            variable=self.x,value=3,width=10,height=1)
        

        label1=tk.Label(frame2,text="请输入视频地址：",font=('Arial',12))
        entry = tk.Entry(frame2, 
            textvariable=self.url, highlightcolor='sky blue', 
            highlightthickness=1, width=35)
        label2=tk.Label(frame2,text=" ")
        play=tk.Button(frame2,text="开始播放",bg='white',
            font=('黑体', 13),
            width=6,height=-1,command=self.videoplay)


        label3=tk.Label(frame2,text="请输入网盘关键词：",font=('Arial',12))
        entry2=tk.Entry(frame2,
            textvariable=self.filename, highlightcolor='sky blue', 
            highlightthickness=1, width=35)
        #label=tk.Label(frame2,text=" ")
        #bp = BitmapImage(file = "c:/Search_128px_1183445_easyicon.net.ico")
        search=tk.Button(frame2,text="搜索资源",bg='white',
            font=('黑体', 13),
            width=6,height=-1,command=self.filesearch)

       
        frame1.pack()
        frame2.pack()

        group.grid(row=0,column=0)
        group2.grid(row=8,column=0)

        tb1.grid(row=0,column=1)
        tb2.grid(row=1,column=1)
        tb3.grid(row=2,column=1)
        tb4.grid(row=3,column=1)
        tb5.grid(row=4,column=1)
        tb6.grid(row=5,column=1)
        tb7.grid(row=6,column=1)
        tb8.grid(row=7,column=1)
        tb9.grid(row=0,column=2)
        tb10.grid(row=1,column=2)
        tb11.grid(row=2,column=2)
        tb12.grid(row=3,column=2)
        tb13.grid(row=4,column=2)
        tb14.grid(row=5,column=2)
        tb15.grid(row=6,column=2)
        tb16.grid(row=7,column=2)


        tb17.grid(row=0,column=3)
        tb18.grid(row=1,column=3)
        tb19.grid(row=2,column=3)
        tb20.grid(row=3,column=3)
        tb21.grid(row=4,column=3)
        tb22.grid(row=5,column=3)
        tb23.grid(row=6,column=3)
        tb24.grid(row=7,column=3)

        tb25.grid(row=8,column=1)
        tb26.grid(row=8,column=2)
        tb27.grid(row=8,column=3)



        label1.grid(row=0,column=0)
        entry.grid(row=0,column=1)
        play.grid(row=0,column=3,ipadx=10,ipady=10)


        label3.grid(row=1,column=0)
        entry2.grid(row=1,column=1)
        search.grid(row=1,column=3,ipadx=10,ipady=10)


    def videoplay(self):
        port_1='http://www.wmxz.wang/video.php?url='
        port_2='http://jx.kdy52.com/?url='
        port_3='http://jx.du2.cc/?url='
        port_4='http://jx.drgxj.com/?url='
        port_5='http://vip.jlsprh.com/?url='
        port_6='http://jx.598110.com/?url='
        port_7='http://jqaaa.com/jx.php?url='
        port_8='http://api.662820.com/xnflv/index.php?url='
        port_9='http://jx.598110.com/zuida.php?url='
        port_10='http://jx.598110.com/duo/index.php?url='
        port_11='https://beaacc.com/api.php?url='
        port_12='http://y.mt2t.com/lines?url='
        port_13='http://jiexi.071811.cc/jx2.php?url='
        port_14='https://api.smq1.com/?url='
        port_15='http://api.91exp.com/svip/?url='
        port_16='http://player.jidiaose.com/supapi/iframe.php?v='

        port_17='http://www.82190555.com/index/qqvod.php?url='
        port_18='http://api.pucms.com/?url='
        port_19='http://api.baiyug.cn/vip/index.php?url='
        port_20='https://api.flvsp.com/?url='
        port_21='http://api.xfsub.com/index.php?url='
        port_22='http://www.82190555.com/index/qqvod.php?url='
        port_23='http://vip.jlsprh.com/index.php?url='
        port_24='http://2gty.com/apiurl/yun.php?url='


        if re.match(r'^https?:/{2}\w.+$',self.url.get()):
            if self.v.get()==1:
                ip=self.url.get()
                webbrowser.open(port_1+ip)
            elif self.v.get()==2:
                ip=self.url.get()
                webbrowser.open(port_2+ip)
            elif self.v.get()==3:
                ip=self.url.get()
                webbrowser.open(port_3+ip)
            elif self.v.get()==4:
                ip=self.url.get()
                webbrowser.open(port_4+ip)
            elif self.v.get()==5:
                ip=self.url.get()
                webbrowser.open(port_5+ip)
            elif self.v.get()==6:
                ip=self.url.get()
                webbrowser.open(port_6+ip)
                        
                
            elif self.v.get()==7:
                ip=self.url.get()
                webbrowser.open(port_7+ip)
            elif self.v.get()==8:
                ip=self.url.get()
                webbrowser.open(port_8+ip)
            elif self.v.get()==9:
                ip=self.url.get()
                webbrowser.open(port_9+ip)
            elif self.v.get()==10:
                ip=self.url.get()
                webbrowser.open(port_10+ip)
            elif self.v.get()==11:
                ip=self.url.get()
                webbrowser.open(port_11+ip)

            elif self.v.get()==12:
                ip=self.url.get()
                webbrowser.open(port_12+ip)
            elif self.v.get()==13:
                ip=self.url.get()
                webbrowser.open(port_13+ip)
            elif self.v.get()==14:
                ip=self.url.get()
                webbrowser.open(port_14+ip)
            elif self.v.get()==15:
                ip=self.url.get()
                webbrowser.open(port_15+ip)
            elif self.v.get()==16:
                ip=self.url.get()
                webbrowser.open(port_16+ip)


            elif self.v.get()==17:
                ip=self.url.get()
                webbrowser.open(port_17+ip)
            elif self.v.get()==18:
                ip=self.url.get()
                webbrowser.open(port_18+ip)
            elif self.v.get()==19:
                ip=self.url.get()
                webbrowser.open(port_19+ip)
            elif self.v.get()==20:
                ip=self.url.get()
                webbrowser.open(port_20+ip)
            elif self.v.get()==21:
                ip=self.url.get()
                webbrowser.open(port_21+ip)
            elif self.v.get()==22:
                ip=self.url.get()
                webbrowser.open(port_22+ip)
            elif self.v.get()==23:
                ip=self.url.get()
                webbrowser.open(port_23+ip)
            elif self.v.get()==24:
                ip=self.url.get()
                webbrowser.open(port_24+ip)



        else:
                msgbox.showerror(title='提示',message='视频地址错误！')


    def filesearch(self):
        #port='http://wjsou.com/s2/'
        port1='https://aizhaomu.com/search/kw'
        port2='http://www.pansoso.com/zh/'
        port3='http://www.pansou.com/?q='
        if self.x.get()==1:
            filename=self.filename.get()
            #name2='.html'
            webbrowser.open(port1+filename)
        elif self.x.get()==2:
            filename=self.filename.get()
            webbrowser.open(port2+filename)
        elif self.x.get()==3:
            filename=self.filename.get()
            webbrowser.open(port3+filename)

    def center(self):
        ws=self.main.winfo_screenwidth()
        hs=self.main.winfo_screenheight()
        x=int((ws/2)-(self.w/2))
        y=int((hs/2)-(self.h/2))
        self.main.geometry('{}x{}+{}+{}'.format
            (self.w,self.h,x,y))
        #self.main.configure(background=self.bg)

    def event(self):
        self.main.resizable(True,True)
        self.center()
        self.main.mainloop()

''' def videoclear(self):
        #self.main.entry.get()
        self.main.entry.delete(0,'end')'''

if __name__ =='__main__':
    app=VideoMenu()
    app.event()

