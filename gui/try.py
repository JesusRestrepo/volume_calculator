import tkinter
x=None
y=None
z=None
cuadro1 = tkinter.Entry(font=("arial",20,),width=22, textvariable=input_text, insertwidth=10, bg="white", justify="right")
cuadro1.place(x=200, y=350)
lbl1 = tkinter.Label(text="Lado 1= ", width=ancho_label, height=alto_label)
lbl1.place(x=75, y=352)
x=cuadro1
cuadro2 = tkinter.Entry(font=("arial",20,),width=22, textvariable=input_text, insertwidth=10, bg="white", justify="right")
cuadro2.place(x=200, y=420)
lbl2 = tkinter.Label(text="Lado 2= ", width=ancho_label, height=alto_label)
lbl2.place(x=75, y=422)
y=cuadro2

cuadro3 = tkinter.Entry(font=("arial",20,),width=22, textvariable=input_text, insertwidth=10, bg="white", justify="right")
cuadro3.place(x=200, y=490)
lbl3 = tkinter.Label(text="Lado 3= ", width=ancho_label, height=alto_label)
lbl3.place(x=75, y=492)
z=cuadro3

def vol_cubo():
    global x
    global y 
    global z
    type(x)
    type(y)
    type(z)
    volumen_cubo=int(x.get())*int(y.get())*int(z.get())
    return var.set(volumen_cubo)