# Desenha apenas uma linha
# Ao desenhar outra, apaga a anterior

from tkinter import *

def marca_inicio(event):
    global ini_x, ini_y
    ini_x = event.x
    ini_y = event.y

def atualiza_fim(event):
    global fim_x, fim_y
    fim_x = event.x
    fim_y = event.y
    canvas.delete("all")
    canvas.create_line(ini_x, ini_y, fim_x, fim_y)


#******* MAIN *******#
ini_x = None 
ini_y = None
fim_x = None
fim_y = None

root = Tk()

canvas = Canvas(root, bg='white', width=600, height=600)
canvas.pack()

canvas.bind('<ButtonPress-1>', marca_inicio)
canvas.bind('<B1-Motion>', atualiza_fim)

root.mainloop()
