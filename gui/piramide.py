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
mystring=tkinter.StringVar(ventana)
date=tkinter.StringVar(ventana)
x=None
y=None

def create_frame():
    root.title("VOLUME CALCULATOR")
    root.iconbitmap(r#"file ubication.ico")
    root.geometry("600x800")
    root.resizable(False,False)
    root.config(bg="gray")

    lbl=tkinter.Label(root,text="PYRAMID VOLUME")
    lbl.config(font="Arial")
    lbl.pack(anchor="center")

    text=tkinter.Label(root,text="pyramid volume= b * h / 3")
    text.pack(anchor="center")

    img_pyramid=ImageTk.PhotoImage(Image.open(path1))
    pyramid=tkinter.Label(root,image=img_pyramid,height=200,width=300)
    pyramid.place(x=150, y=100)

    entry1 = tkinter.Entry(root, font=("arial",20,),width=22, textvariable=mystring, insertwidth=10, bg="white", justify="right")
    entry1.place(x=200, y=350)
    lbl1 = tkinter.Label(root, text="B= ", width=width_label, height=height_label)
    lbl1.place(x=75, y=352)
    x=entry1
    global x

    entry2 = tkinter.Entry(root, font=("arial",20,),width=22, textvariable=date, insertwidth=10, bg="white", justify="right")
    entry2.place(x=200, y=420)
    lbl2 = tkinter.Label(root, text="H= ", width=width_label, height=height_label)
    lbl2.place(x=75, y=422)
    y=entry2
    global y

    buttoncalculate = tkinter.Button(root, text="CALCULATE", bg="white", width=10, height=2, command=vol_pyramid)
    buttoncalculate.place(x=250, y=490)

    total = tkinter.Entry(root, font=("arial",20,),width=22, textvariable=result, insertwidth=10, bg="white", justify="right")
    total.place(x=200, y=560)
    lbltotal = tkinter.Label(root, text="TOTAL= ", width=width_label, height=height_label)
    lbltotal.place(x=75, y=562)

    buttonreturn = tkinter.Button(root, text="RETURN", bg="white", width=10, height=2, command=regresar)
    buttonreturn.place(x=250, y=700)

    root.mainloop()

def regresar():
    interfaz.create_frame()

def vol_pyramid():
    b=int(x.get())
    h=int(y.get())
    volume_pyramid=b*h/3
    result.set(volume_pyramid)