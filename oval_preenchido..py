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
        ovals.append((ini_x, ini_y, fim_x, fim_y,cor_atual))
    desenhar()


def desenhar():
    canvas.delete("all")
    for x1, y1, x2, y2,cor in ovals:
        canvas.create_oval(x1, y1, x2, y2,outline = "black",fill= cor, width=2)  


def muda_cor(nova_cor):
    global cor_atual
    cor_atual = nova_cor


ovals = []
ini_x = ini_y = 0
cor_atual = 'blue'

root = Tk()
root.title("Oval_preenchido")

canvas = Canvas(root, bg='white', width=600, height=600)
canvas.pack()


frame_botao = Frame(root)
frame_botao.pack(fill= "x",pady=5)

botao_azul = Button(frame_botao,text="Azul",command= lambda: muda_cor("blue"))
botao_azul.pack(side=LEFT, expand=True, fill="x", padx=5)

botao_amarelo = Button(frame_botao,text="Amarelo",command= lambda: muda_cor("yellow"))
botao_amarelo.pack(side=LEFT, expand= True, fill="x",padx=5)

botao_vermelho = Button(frame_botao,text= "Vermelho",command= lambda: muda_cor("red"))
botao_vermelho.pack(side=LEFT, expand = True,fill ="x",padx=5)


canvas.bind('<ButtonPress-1>', inicia_linha)
canvas.bind('<B1-Motion>', arrastar)
canvas.bind('<ButtonRelease-1>', incluir_oval)

root.mainloop()
