from tkinter import *


def inicia_linha(event):
    global ini_x, ini_y 
    ini_x = event.x
    ini_y = event.y


def arrastar(event):
    fim_x = event.x
    fim_y = event.y
    desenhar()
    canvas.create_oval(
    ini_x, ini_y,
    fim_x, fim_y,
    dash=(4, 2)
        )


def incluir_oval(event):
    fim_x = event.x
    fim_y = event.y
    if ini_x != fim_x and ini_y != fim_y:
        ovals.append((ini_x, ini_y, fim_x, fim_y))
    desenhar()


def desenhar():
    canvas.delete("all")
    for (x1, y1, x2, y2) in ovals:
        canvas.create_oval(x1, y1, x2, y2, width=2)  

ovals = []
ini_x = ini_y = 0

root = Tk()
root.title("Oval")

canvas = Canvas(root, bg='white', width=600, height=600)
canvas.pack()

ini_x = ini_y = fim_x = fim_y = None

ini_x = None
ini_y = None
fim_x = None
fim_y = None
canvas.bind('<ButtonPress-1>', inicia_linha)
canvas.bind('<B1-Motion>', arrastar)
canvas.bind('<ButtonRelease-1>', incluir_oval)

root.mainloop()