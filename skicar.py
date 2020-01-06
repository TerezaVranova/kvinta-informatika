import tkinter
from random import randrange, randint
x_max,y_max=800,600
canvas=tkinter.Canvas(width=x_max,height=y_max,bg="white")
canvas.pack()

x1,y1=0,0
farba,hrubka="blue",2

def klik(event):
    global x1,y1
    x1,y1=event.x,event.y

    x,y=event.x,event.y
    global farba,hrubka
    if x <= 50 and 50 > y >= 0:
        farba="blue"
    elif x <= 50 and 100 > y >= 50:
        farba="red"
    elif x <= 50 and 150 >= y >= 100:
        farba="yellow"
    else:
        pass

    if x <= 50 and 250 > y >= 200:
        hrubka=2
    elif x <= 50 and 300 > y >= 250:
        hrubka=4
    elif x <= 50 and 350 >= y >= 300:
        hrubka=8
    else:
        pass

    if x <= 50 and 450 >= y >= 400:
        canvas.delete("all")
        tlacidla()

def kreslenie(event):
    x,y=event.x,event.y
    global x1,y1
    canvas.create_line(x1,y1,x,y,width=hrubka,fill=farba)
    x1,y1=x,y

def tlacidla():
    canvas.create_rectangle(0,0,50,50,fill="blue")
    canvas.create_rectangle(0,50,50,100,fill="red")
    canvas.create_rectangle(0,100,50,150,fill="yellow")

    canvas.create_rectangle(0,200,50,250)
    canvas.create_oval(25-2,225-2,25+2,225+2,fill="black")
    canvas.create_rectangle(0,250,50,300)
    canvas.create_oval(25-4,275-4,25+4,275+4,fill="black")
    canvas.create_rectangle(0,300,50,350)
    canvas.create_oval(25-8,325-8,25+8,325+8,fill="black")
    
    canvas.create_rectangle(0,400,50,450)
    canvas.create_text(25,425,font="Arial 10",text="RESET")
    
canvas.bind("<B1-Motion>",kreslenie)
canvas.bind("<Button-1>", klik)
tlacidla()
