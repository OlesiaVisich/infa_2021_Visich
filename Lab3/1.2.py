from graph import *
import math


#начальный фон
penColor(51, 255, 255)
brushColor(51, 255, 255)
rectangle(0, 0, 500, 200)
penColor(51, 51, 205)
brushColor(51, 51, 205)
rectangle(0, 200, 500, 300)
penColor('yellow')
brushColor('yellow')
rectangle(0, 300, 500, 450)
windowSize(500, 450)
#солнце
penColor('yellow')
brushColor('yellow')
circle(400, 80, 40)
for i in range(0, 96, 2):
    y1=80-40*math.sin(i*3.14/24)
    x1=400+40*math.cos(i*3.14/24)
    y2=80-50*math.sin((i+1)*3.14/24)
    x2=400+50*math.cos((i+1)*3.14/24)
    y3=80-40*math.sin((i+2)*3.14/24)
    x3=400+40*math.cos((i+2)*3.14/24)
    polygon([(x1, y1), (x2, y2), (x3, y3), (x1, y1)])

#облака    
penColor('blue')
brushColor('white')
for i in range (30, 120, 30):
    circle(60+i, 50, 20)
circle(170, 70, 20)
for i in range (30, 120, 30):
    circle(50+i, 70, 20)

for i in range (160, 250, 30):
    oval(60+i, 70, 100+i, 20)
oval(300, 90, 340, 40)
for i in range (150, 240, 30):
    oval(60+i, 90, 100+i, 40)
    
for i in range (50, 140, 30):
    oval(60+i, 130, 100+i, 100)
oval(190, 149, 230, 120)
for i in range (40, 130, 30):
    oval(60+i, 150, 100+i, 120)

#дуги волн
penColor('yellow')
brushColor('yellow')
for i in range(5):
    x=50+100*i
    circle(x, 340, 50)   
penColor(51, 51, 205)
brushColor(51, 51, 205)
for i in range(6):
    x=100*i
    circle(x, 253, 50)
penColor('white')
line(0, 297, 500, 297)
#кораблик
brushColor('brown')
rectangle(270, 225, 450, 263)
penColor(51, 51, 205)
brushColor(51, 51, 205)
rectangle(270, 260, 450, 270)
brushColor('brown')
penColor('brown')
circle(270, 225, 34)
penColor(51, 51, 205)
brushColor(51, 51, 205)
rectangle(200, 200, 500, 225)
penColor(51, 255, 255)
brushColor(51, 255, 255)
rectangle(200, 199, 500, 150)
penSize(40)
penColor(51, 51, 205)
line(410, 280, 460, 225)
penColor('black')
penSize(5)
line(320, 226, 320, 100)
penSize(2)
penColor('black')
brushColor('white')
polygon([(320, 100), (380, 160),
        (340, 160), (320, 100)])
polygon([(320, 220), (380, 160),
         (340, 160), (320, 220)])
penSize(4)
circle(400, 240, 7)
#mini
x=-200
y=-20
penColor('brown')
brushColor('brown')
rectangle(270+x, 220+y, 350+x, 240+y)

circle(270+x, 220+y, 20)

penColor(51, 255, 255)
brushColor(51, 255, 255)
rectangle(0, 199, 300, 160)
penColor(51, 51, 205)
brushColor(51, 51, 205)
penSize(1)
polygon([(351+x,221+y), (351+x, 241+y), (331+x, 241+y), (351+x,221+y)])
penColor('black')
penSize(5)
line(290+x, 221+y, 290+x, 150+y)
penSize(2)
penColor('black')
brushColor('white')
x=x-30
y=y+50
polygon([(320+x, 100+y), (380+x, 130+y),
        (340+x, 130+y), (320+x, 100+y)])
y=y-30
polygon([(320+x, 195+y), (380+x, 160+y),
         (340+x, 160+y), (320+x, 195+y)])
penSize(2)
x=x-40
y=y-30
circle(400+x, 240+y, 4)
#зонтик
penSize(6)
penColor('brown')
line(80, 400, 80, 260)
penColor(255, 51, 102)
brushColor(255, 51, 102)
penSize(2)
polygon([(20,290), (77, 260), (83, 260), (140, 290)])
penSize(1)
penColor('blue')
rectangle(77, 259, 83, 290)
penColor('black')
for i in range (20, 77, 15):
    line(77, 260, i, 290)
for i in range (83, 140, 15):
    line(83, 260, i, 290)
#mini
penSize(3)
penColor('brown')
x=120
y=-10
line(80+x, 400+y, 80+x, 300+y)
penColor(255, 51, 102)
brushColor(255, 51, 102)
penSize(2)
y=y+40
polygon([(40+x,280+y), (77+x, 260+y), (83+x, 260+y), (120+x, 280+y)])
penSize(1)
penColor('blue')
rectangle(77+x, 259+y, 83+x, 280+y)
penColor('black')
for i in range (40, 77, 10):
    line(77+x, 260+y, i+x, 280+y)
for i in range (83, 120, 10):
    line(83+x, 260+y, i+x, 280+y)

run()