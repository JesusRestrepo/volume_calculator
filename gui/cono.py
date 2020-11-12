import tkinter
import math
import sys
from PIL import Image, ImageTk
from gui import interfaz

input_text=str()
root = tkinter.Toplevel()
path1=#"file ubication"
width_label = 15
height_label = 2
result=tkinter.StringVar()
mystring=tkinter.StringVar(root)
date=tkinter.StringVar(root)
x=None
y=None

def create_frame():
    root.title("VOLUME CALCULATOR")
    root.iconbitmap(r#"file ubication.ico")
    root.geometry("600x800")
    root.resizable(False,False)
    root.config(bg="gray")

    lbl=tkinter.Label(root,text="CONE VOLUME")
    lbl.config(font="Arial")
    lbl.pack(anchor="center")

    text=tkinter.Label(root,text="cone volume= π*R^2*h/3")
    text.pack(anchor="center")

    img_cone=ImageTk.PhotoImage(Image.open(path1))
    cone=tkinter.Label(root,image=img_cone,height=300,width=300)
    cone.place(x=150, y=100)

    entryR = tkinter.Entry(root, font=("arial",20,),width=22, textvariable=mystring, insertwidth=10, bg="white", justify="right")
    entryR.place(x=200, y=450)
    lblR = tkinter.Label(root, text="R= ", width=width_label, height=height_label)
    lblR.place(x=75, y=452)
    x=entryR
    global x

    entryh = tkinter.Entry(root, font=("arial",20,),width=22, textvariable=date, insertwidth=10, bg="white", justify="right")
    entryh.place(x=200, y=520)
    lblh = tkinter.Label(root, text="h= ", width=width_label, height=height_label)
    lblh.place(x=75, y=522)
    y=entryh
    global y

    buttoncalculate = tkinter.Button(root, text="CALCULATE", bg="white", width=10, height=2, command=vol_cone)
    buttoncalculate.place(x=250, y=590)

    total = tkinter.Entry(root, font=("arial",20,),width=22, textvariable=result, insertwidth=10, bg="white", justify="right")
    total.place(x=200, y=660)
    lbltotal = tkinter.Label(root, text="TOTAL= ", width=width_label, height=height_label)
    lbltotal.place(x=75, y=662)

    buttonreturn = tkinter.Button(root, text="RETURN", bg="white", width=10, height=2, command=regresar)
    buttonreturn.place(x=250, y=730)

    root.mainloop()

def regresar():
    interfaz.create_frame()

def vol_cone():
    r=int(x.get())
    h=int(y.get())
    volume_cone=(math.pi*r**2*h)/3
    result.set(volume_cone)