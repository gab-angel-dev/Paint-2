from tkinter import *


def inicia_linha(event):
    global ini_x, ini_y, raio
    ini_x = event.x
    ini_y = event.y


def atualiza_linha(event):
    global fim_x, fim_y, raio
    fim_x = event.x
    fim_y = event.y
    desenhar()
    raio = ((ini_x - fim_x)**2 + (ini_y - fim_y)**2) **0.5
    canvas.create_oval(ini_x-raio, ini_y-raio,fim_x+ raio,fim_y + raio,dash = (4,2))


def incluir_circulo(event):
    if raio > 0:
        circulos.append((ini_x, ini_y, raio, cor_atual))
    desenhar()

def desenhar():
    canvas.delete("all")
    for circulo in circulos:
        x,y,r,cor = circulo
        canvas.create_oval(x-r, y-r, x+r,y+r,outline = "black",fill= cor,width = 3)


def muda_cor(nova_cor):
    global cor_atual
    cor_atual = nova_cor


circulos = []
raio = 0
ini_x = 0
ini_y = 0
cor_atual = "blue"


root = Tk()
root.title("Circulos_coloridos")

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
canvas.bind('<B1-Motion>', atualiza_linha)
canvas.bind('<ButtonRelease-1>', incluir_circulo)

root.mainloop()