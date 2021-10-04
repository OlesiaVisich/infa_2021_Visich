from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
    
colors = ['red', 'orange', 'yellow', 'green', 'blue']

#создает шарик
def new_ball():
    global x,y,r
    canv.delete(ALL)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    canv.create_oval(x-r, y-r, x+r, y+r, fill=choice(colors), width=0)
    root.after(1000, new_ball)
        
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