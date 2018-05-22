#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *  #控件基础包，导入这个包后，这个包下的所有函数可以直接调用

def test1():
    root=Tk()
    frame=Frame(root,width=150,height=350)
    label=Label(frame,text='Emtered :')
    label.pack()
    def enter(event):
        #label['text']='Entered Frame:x=%d y=%d'%(event.x,event.y)
        label.configure(text='Entered Frame:x=%d y=%d'%(event.x,event.y))
    frame.bind('<Any-Enter>',enter)
    frame.pack()
    root.mainloop()
def test2():
    root=Tk()
    for relief in [RAISED,SUNKEN,FLAT,RIDGE,GROOVE,SOLID]:
        f=Frame(root,borderwidth=2,relief=relief)
        Label(f,text=relief,width=10).pack(side=LEFT)
        f.pack(side=LEFT,padx=5,pady=5)
    root.mainloop()
def test3():
    root=Tk()
    f=Frame(root,width=200,height=110)
    xf=Frame(f,relief=GROOVE,borderwidth=2)
    Label(xf,text='You shot him!').pack(pady=10)
    Button(xf,text='''He's dead''',state=DISABLED).pack(side=LEFT,padx=5,pady=8)
    Button(xf,text='''He's good''',command=root.quit).pack(side=RIGHT,padx=5,pady=8)
    xf.place(relx=0.01,rely=0.0125,anchor=NW)
    Label(f,text='self--defind').place(relx=.06,rely=0.0125,anchor=W)
    f.pack()
    root.mainloop()
def test4():
    root=Tk()
    Label(root,text='Anagram:').pack(side=LEFT,padx=5,pady=10)
    e=StringVar()
    entry=Entry(root,width=40,textvariable=e).pack(side=LEFT)
    e.set('hello my name is liang qian wu')
    var=IntVar()
    rF=Frame(root,borderwidth=2)
    rF.pack(side=BOTTOM,padx=5,pady=5)
    for text,value in[('Passin fruit',1),('Apples',2),('Oranges',3)]:
        Radiobutton(rF,text=text,value=value,variable=var,command=lambda se=e,i=var:se.set('select: %d '%i.get())).pack(anchor=NW)
    var.set(3)
    for text,value in[('Red',1),('Tilsit',2),('Brie',3)]:
        Radiobutton(rF,text=text,value=value,variable=var,indicatoron=0).pack(anchor=W,fill=X,padx=18)
    var.set(3)
    root.mainloop()
def test5():
    root=Tk()
    var=IntVar()
    for castmember,row,col,status in[('Passin fruit',0,0,NORMAL),('Apples',0,1,NORMAL),('Oranges',1,0,DISABLED),
                                     ('Terry Jones',1,1,NORMAL)]:
        Checkbutton(root,text=castmember,state=status,variable=(var,castmember),
                    anchor=NW).grid(row=row,column=col,sticky=W)
    root.mainloop()
def test6():
    root=Tk()
    text=Text(root,height=26,width=50)
    scroll=Scrollbar(root,command=text.yview)
    text.configure(yscrollcommand=scroll.set)
    text.tag_configure('bold_italics',font=('Verdane',12,'bold','italic'))
    text.tag_configure('big',font=('Verdane',24,'bold'))
    text.tag_configure('color',foreground='blue',font=('Tempus Sans ITC',14))
    text.tag_configure('groove',relief=GROOVE,borderwidth=2)
    text.tag_bind('bite','<1>',lambda e,t=text:t.insert(END,"I'll bite your legs off!"))
    text.insert(END,'something up with my banter,chaps?\n')
    text.insert(END,'Four hours to bury a cat?\n','bold_italics')
    text.insert(END,'Cat I call you Frank?\n','big')
    text.insert(END,'Cat I call you Frank?\n','color')
    text.insert(END,'Cat I call you Frank?\n','groove')
    button=Button(text,text='I do live at 46')
    text.window_create(END,window=button)
    text.pack(side=LEFT)
    scroll.pack(fill=Y)
    root.mainloop()
def test7():
    root=Tk()
    canvas=Canvas(root,width=400,height=400)
    canvas.create_oval(10,10,100,100,fill='gray90')
    canvas.create_text(350,100,text='text',fill='yellow')
    frm=Frame(canvas,relief=GROOVE,borderwidth=2)
    Label(frm,text='Embedded Frame/Label').pack()
    canvas.create_window(285,280,window=frm,anchor=CENTER)
    canvas.pack()
    root.mainloop()
def test8():
    root=Tk()
    list=Listbox(root,width=15,height=6)
    #scroll=Scrollbar(root,command=list.yview)
    #list.configure(yscrollcommand=scroll.set)
    list.pack(side=LEFT)
    #scroll.pack(side=RIGHT,fill=Y)
    for item in range(30):
        list.insert(END,item)
    root.mainloop()
def test9():
    root=Tk()
    label=Label(root,text="h=")
    scale=Scale(root,orient=VERTICAL,length=284,from_=0,to=250,tickinterval=50,command=lambda h,l=label:l.configure(text='h=%s'%h))
    label.pack(side=LEFT)
    scale.pack(side=LEFT)
    root.mainloop()
if __name__ =='__main__':
    test8()