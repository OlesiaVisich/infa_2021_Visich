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
k=[1]*7
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
	for i in range (5):
		if x[i]>=15 and x[i]<=680 and y[i]>=15 and y[i]<=480:
			x[i]=x[i]+a[i]
			y[i]=y[i]+b[i]
		if x[i]<15 :
			a[i]=-a[i]
			x[i]=x[i]+a[i]

		if y[i]<15:
			b[i]=-b[i]
			y[i]=y[i]+b[i]
		if x[i]>680:
			a[i]=-a[i]
			x[i]=x[i]+a[i]
		if y[i]>480:
			b[i]=-b[i]
			y[i]=y[i]+b[i]
		canv.create_oval(x[i]-r[i], y[i]-r[i], x[i]+r[i], y[i]+r[i], fill=colors[i], width=0)
	i=6
	while i==6:
		if x[i]>=15 and x[i]<=680 and y[i]>=15 and y[i]<=480:
			x[i]=x[i]+a[i]
			y[i]=y[i]+b[i]
		if x[i]<15 :
			a[i]=-a[i]
			x[i]=x[i]+a[i]

		if y[i]<15:
			b[i]=-b[i]
			y[i]=y[i]+b[i]
		if x[i]>680:
			a[i]=-a[i]
			x[i]=x[i]+a[i]
		if y[i]>480:
			b[i]=-b[i]
			y[i]=y[i]+b[i]
		canv.create_rectangle(x[i]-r[i], y[i]-r[i], x[i]+r[i], y[i]+r[i], fill=colors[i], width=0)
		i=i+1
	'''for i in range (6,7):
			 x[i]>=15 and x[i]<=680 and y[i]>=15 and y[i]<=480:
			x[i]=x[i]+a[i]
			y[i]=y[i]+b[i]
			 x[i]<15 :
			a[i]=-a[i]
			x[i]=x[i]+a[i]
			 y[i]<15:
			b[i]=-b[i]
			y[i]=y[i]+b[i]
			 x[i]>680:
			a[i]=-a[i]
			x[i]=x[i]+a[i]
			 y[i]>480:
			b[i]=-b[i]
			y[i]=y[i]+b[i]
		canv.create_rectangle(x[i]-r[i], y[i]-r[i], x[i]+r[i], y[i]+r[i], fill=colors[i], width=0)'''
	w=0
	for i in range (7):
		w=w+k[i]
	if w==1:
		canv.create_rectangle(10, 80, 300, 150, fill='yellow', outline='green',
                       width=3)
		canv.create_text(200, 115, text="total points: "+str(p), anchor=SE, font="Verdana 14", fill="grey")
	#print ('WHY', w)
	job=root.after(100, move)
	
def new_ball():
	global x,y,r,a,b,job
	if job:
		root.after_cancel(job)
		job=None
	for i in range (7):
		x[i]=rnd(100,500)
		y[i]=rnd(100,400)
	move()
	
p=0
w=0

#попал или нет
def click(event):
	global p
	fl=False
	x1=event.x
	y1=event.y
	for i in range (7):
		r1=((x1-x[i])**2+(y1-y[i])**2)**0.5
		if (r1<r[i]):
			if (i<=5):
				print('True')
				p=p+10
				print(p)
				fl=True
			else:
				print('True')
				p=p+30
				print(p)
				fl=True
			r[i]=0
			k[i]=0
			
		else:
			print('False')
	if not fl:
		p=p-1

	'''w=0
	for i in range (7):
		w=w+r[i]
	if w==0:
		for i in range (7):
			r[i]=rnd(30,50)
		new_ball()'''

new_ball()
canv.bind('<Button-1>', click)

#new_ball()
mainloop()
