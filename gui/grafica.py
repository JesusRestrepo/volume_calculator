import tkinter
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
ventana=tkinter.Tk()
ventana.title("CALCULADORA DE VOLÚMENES")
#ventana.iconbitmap(r"/home/chucho/Documentos/calculadora_volumenes/imagenes/Calculator_30001.ico")
ventana.geometry("600x800")
ventana.resizable(False,False)
ventana.config(bg="gray")

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

u = np.linspace(-1, 2, 60)
v = np.linspace(0, 2*np.pi, 60)
U, V = np.meshgrid(u, v)

X = U
Y1 = (3*u**2 + 1)*np.cos(V)
Z1 = (3*U**2 + 1)*np.sin(V)

Y2 = (U + 3)*np.cos(V)
Z2 = (U + 3)*np.sin(V)

ax.plot_surface(X, Y1, Z1, alpha=0.3, color='red', rstride=6, cstride=12)
ax.plot_surface(X, Y2, Z2, alpha=0.3, color='blue', rstride=6, cstride=12)
plt.show()

ventana.mainloop()