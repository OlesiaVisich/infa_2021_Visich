from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
    
colors = ['red']
#, 'orange', 'yellow', 'green', 'blue'
#создает шарик
x = rnd(100,700)
y = rnd(100,500)
r = rnd(30,50)
a=5
b=5
job=None
def move():
    global x,y,a,b,job
    canv.delete(ALL)
    if x>=15 and x<=680 and y>=15 and y<=480:
        x=x+a
        y=y+b
    if x<15 :
        a=-a
        x=x+a
        #b=-b
        #x=16
    if y<15:
        #a=-a
        b=-b
        y=y+b
        #y=16
    if x>680:
        a=-a
        x=x+a
        #b=-b
        #x=679
    if y>480:
        #a=-a
        b=-b
        y=y+b
        #y=479
    canv.create_oval(x-r, y-r, x+r, y+r, fill=choice(colors), width=0)
    job=root.after(100, move)
    
def new_ball():
    global x,y,r,a,b,job
    if job:
        root.after_cancel(job)
        job=None
    x=rnd(100,500)
    y=rnd(100,400)
    #a=rnd(-5,5)
    #b=rnd(-5,5)
    move()

    #a=rnd(0,10)
    #b=rnd(0,10
    
        
p=0
#попал или нет
def click(event):
    global p
    x1=event.x
    y1=event.y
    r1=((x1-x)**2+(y1-y)**2)**0.5
    if (r1<r):
        print('True')
        p=p+10
        print(p)
        new_ball()
    else:
        print('False')
    #print(x,y,r)
    #print()
    #print(x1, y1, r1)
    #print()

new_ball()
canv.bind('<Button-1>', click)

        
new_ball()
mainloop()