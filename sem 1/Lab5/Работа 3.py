from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
    
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'black', 'brown']
#создает шарик
x=[0,0,0,0,0,0,0]
y=[0,0,0,0,0,0,0]
r=[0,0,0,0,0,0,0]
a=[0,0,0,0,0,0,0]
b=[0,0,0,0,0,0,0]
job=None
for i in range (7):
    x[i] = rnd(100,700)
    y[i] = rnd(100,500)
    r[i] = rnd(30,50)
    a[i] = rnd(-15,15)
    b[i] = rnd(-15,15)

def move():
    global x,y,a,b,job
    canv.delete(ALL)
    for i in range (7):
        if x[i]>=15 and x[i]<=680 and y[i]>=15 and y[i]<=480:
            x[i]=x[i]+a[i]
            y[i]=y[i]+b[i]
        if x[i]<15 :
            a[i]=-a[i]
            x[i]=x[i]+a[i]
        #b=-b
        #x=16
        if y[i]<15:
        #a=-a
            b[i]=-b[i]
            y[i]=y[i]+b[i]
        #y=16
        if x[i]>680:
            a[i]=-a[i]
            x[i]=x[i]+a[i]
        #b=-b
        #x=679
        if y[i]>480:
        #a=-a
            b[i]=-b[i]
            y[i]=y[i]+b[i]
        #y=479
        canv.create_oval(x[i]-r[i], y[i]-r[i], x[i]+r[i], y[i]+r[i], fill=colors[i], width=0)
    job=root.after(100, move)
    
def new_ball():
    global x,y,r,a,b,job
    if job:
        root.after_cancel(job)
        job=None
    for i in range (7):
        x[i]=rnd(100,500)
        y[i]=rnd(100,400)
    #a=rnd(-5,5)
    #b=rnd(-5,5)
    move()

    #a=rnd(0,10)
    #b=rnd(0,10
    
        
p=0
w=0
#попал или нет
def click(event):
    global p
    x1=event.x
    y1=event.y
    for i in range (7):
        r1=((x1-x[i])**2+(y1-y[i])**2)**0.5
        if (r1<r[i]):
            print('True')
            p=p+10
            print(p)
            #new_ball()
            r[i]=0
            
        else:
            print('False')
    w=0
    for i in range (7):
        w=w+r[i]
    if w==0:
        for i in range (7):
            r[i]=rnd(30,50)
        new_ball()
    #print(x,y,r)
    #print()
    #print(x1, y1, r1)
    #print()

new_ball()
canv.bind('<Button-1>', click)

        
new_ball()
mainloop()