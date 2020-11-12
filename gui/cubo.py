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
var=tkinter.StringVar(root)
mystring=tkinter.StringVar(root)
date=tkinter.StringVar(root)
result=tkinter.StringVar()
x=None
y=None
z=None

def create_frame():
    root.title("VOLUME CALCULATOR")
    root.iconbitmap(os.path.join(sys.path[0], #"file ubication.ico")
    root.geometry("600x800")
    root.resizable(False,False)
    root.config(bg="gray")

    lbl=tkinter.Label(root,text="CUBE VOLUME")
    lbl.config(font="Arial")
    lbl.pack(anchor="center")

    text=tkinter.Label(root,text="cube volume= side * side * side")
    text.pack(anchor="center")

    img_cube=ImageTk.PhotoImage(Image.open(path1))
    cube=tkinter.Label(root,image=img_cube,height=200,width=300)
    cube.place(x=150, y=100)

    entry1 = tkinter.Entry(root, font=("arial",20,),width=22, textvariable=var, insertwidth=10, bg="white", justify="right")
    entry1.place(x=200, y=350)
    lbl1 = tkinter.Label(root, text="side 1= ", width=width_label, height=height_label)
    lbl1.place(x=75, y=352)
    x=entry1
    global x

    entry2 = tkinter.Entry(root, font=("arial",20,),width=22, textvariable=date, insertwidth=10, bg="white", justify="right")
    entry2.place(x=200, y=420)
    lbl2 = tkinter.Label(root, text="side 2= ", width=width_label, height=height_label)
    lbl2.place(x=75, y=422)
    y=entry2
    global y

    entry3 = tkinter.Entry(root, font=("arial",20,),width=22, textvariable=mystring, insertwidth=10, bg="white", justify="right")
    entry3.place(x=200, y=490)
    lbl3 = tkinter.Label(root, text="Lado 3= ", width=width_label, height=height_label)
    lbl3.place(x=75, y=492)
    z=entry3
    global z

    buttoncalculate = tkinter.Button(root, text="CALCULATE", bg="white", width=10, height=2, command=vol_cube)
    buttoncalculate.place(x=250, y=560)

    total = tkinter.Entry(root, font=("arial",20,),width=22, textvariable=result, insertwidth=10, bg="white", justify="right")
    total.place(x=200, y=630)
    lbltotal = tkinter.Label(root, text="total= ", width=ancho_label, height=alto_label)
    lbltotal.place(x=75, y=632)

    buttonreturn = tkinter.Button(root, text="RETURN", bg="white", width=10, height=2, command=regresar)
    buttonreturn.place(x=250, y=700)

    root.mainloop()

def vol_cube():
    volume_cube=int(x.get())*int(y.get())*int(z.get())
    result.set(volume_cube)

def regresar():
    interfaz.create_frame()