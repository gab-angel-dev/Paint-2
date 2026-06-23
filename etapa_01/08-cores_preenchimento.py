from tkinter import *
from tkinter import ttk



# Quando mouse é pressionado
def iniciar_figura_nova(event): 
    global figura_nova
    global cor_escolhida
    global cor_escolhida_preenchimento
    cor_outline = get_color(cor_escolhida)
    cor_fill = get_color(cor_escolhida_preenchimento)
    
    if tipo_figura_var.get() == 'Linha':
        figura_nova = ("linha", (event.x, event.y, event.x, event.y), cor_outline, cor_fill)
    elif tipo_figura_var.get() == 'Rabisco':
        figura_nova = ("rabisco", [(event.x, event.y)], cor_outline, cor_fill)
    elif tipo_figura_var.get() == 'Retângulo':
        figura_nova = ('retangulo', (event.x, event.y, event.x, event.y), cor_outline, cor_fill)
    elif tipo_figura_var.get() == 'Oval':
        figura_nova = ('oval', (event.x, event.y, event.x, event.y), cor_outline, cor_fill)
    elif tipo_figura_var.get() == 'Círculo':
        figura_nova = ('circulo', (event.x , event.y, event.x, event.y), cor_outline, cor_fill)
    
# Quando mouse é movido com o botão pressionado
def atualizar_figura_nova(event):
    global figura_nova
    global cor_escolhida
    global cor_escolhida_preenchimento
    cor_outline = get_color(cor_escolhida)
    cor_fill = get_color(cor_escolhida_preenchimento)
    global raio
    if figura_nova[0] == "rabisco":
        figura_nova[1].append((event.x, event.y))
    elif figura_nova[0] == "linha":
        figura_nova = ("linha", (figura_nova[1][0], figura_nova[1][1], event.x, event.y), cor_outline, cor_fill)
    elif figura_nova[0] == 'retangulo':
        figura_nova = ('retangulo', (figura_nova[1][0], figura_nova[1][1], event.x, event.y), cor_outline, cor_fill)
    elif figura_nova[0] == 'oval':
        figura_nova = ('oval', (figura_nova[1][0], figura_nova[1][1], event.x, event.y), cor_outline, cor_fill)
    elif figura_nova[0] == 'circulo':
        raio = min(
        abs(event.x-figura_nova[1][0]),
        abs(event.y-figura_nova[1][1])
        )
        figura_nova = ('circulo', (figura_nova[1][0], figura_nova[1][1], figura_nova[1][0]+raio, figura_nova[1][1]+raio), cor_outline, cor_fill)
    
    desenhar_figuras()
    desenhar_figura_nova()

# Quando mouse é solto
def incluir_figura_nova(event): 
    if not incompleta(figura_nova): # para evitar incluir figuras incompletas, como uma linha sem comprimento ou um rabisco com um único ponto
        figuras.append(figura_nova) 
    desenhar_figuras()

# Cria as figuras 
def desenhar_figuras():
    canvas.delete("all")
    for fig, values, cor_outline, cor_fill in figuras:
        if fig == "linha":
            canvas.create_line(values[0], values[1], values[2], values[3])
        elif fig == "rabisco":
            canvas.create_line(values)
        elif fig == 'retangulo':
            canvas.create_rectangle(values, outline=cor_outline, fill=cor_fill ,width=2)
        elif fig == 'oval':
            canvas.create_oval(values, outline=cor_outline, fill=cor_fill, width=2)
        elif fig == 'circulo':
            canvas.create_oval(values, outline=cor_outline, fill=cor_fill, width=2)

def desenhar_figura_nova():
    if len(figura_nova) == 4:
        fig, values, cor_outline, cor_fill = figura_nova
    else:
        fig, values = figura_nova
    if fig == "linha":
        canvas.create_line(values[0], values[1], values[2], values[3], dash=(4, 2))
    elif fig == "rabisco":
        canvas.create_line(values, dash=(4, 2))
    elif fig == "retangulo":
        canvas.create_rectangle(values, dash=(4, 2), outline=cor_outline, fill=cor_fill ,width=2)
    elif fig == "oval":
        canvas.create_oval(values, dash=(4, 2), outline=cor_outline, fill=cor_fill, width=2)
    elif fig == "circulo":
        canvas.create_oval(values, dash=(4, 2), outline=cor_outline, fill=cor_fill, width=2)


def incompleta(figura):
    fig, values, cor_outline, cor_fill = figura
    if fig == "linha":
        return (values[0], values[1]) == (values[2], values[3])
    elif fig == "retangulo":
        return (values[0], values[1]) == (values[2], values[3])
    elif fig == "oval":
        return (values[0], values[1]) == (values[2], values[3])
    elif fig == 'circulo':
            return (values[0], values[1]) == (values[2], values[3])
    elif fig == "rabisco":
        return len(values) <= 1

# cores
def get_color(cor):
    if cor.get() == 'Preto':
        return 'black'
    elif cor.get() == 'Branco':
        return 'white'
    elif cor.get() == 'Amarelo':
        return 'yellow'
    elif cor.get() == 'Azul':
        return 'blue'
    elif cor.get() == 'Verde':
        return 'green'
    elif cor.get() == 'Vermelho':
        return 'red'
    elif cor.get() == 'Rosa':
        return 'pink'




#******* MAIN *******#

figuras = []       # Todas as figuras desenhadas
figura_nova = None # Figura que está sendo desenhada, mas ainda não foi incluída em figuras
cor = None
raio = 0

root = Tk()
root.title('Exemplo de aplicação')
frame = Frame(root)

# Widgets arranjados com Layout grid dentro de frame
paddings = {'padx': 2, 'pady': 2} 

# label
label = ttk.Label(frame,  text='Escolha se vai desenhar linha ou Rabisco:')
label.grid(column=0, row=0, sticky=W, **paddings)

# option menu
tipo_figura_var = StringVar(root) # Guarda o tipo de figura selecionado no option menu (linha ou rabisco)
option_menu = ttk.OptionMenu(
    frame, tipo_figura_var,
    'Linha',
    'Linha',
    'Rabisco',
    'Retângulo',
    'Oval',
    'Círculo')

option_menu.grid(column=2, row=0, sticky=W, **paddings)

cor_escolhida = StringVar(root) 
menu_colors =  ttk.OptionMenu(
    frame, cor_escolhida,
    'Preto',
    'Preto',
    'Branco',
    'Amarelo',
    'Azul',
    'Verde',
    'Vermelho',
    'Rosa'
)
menu_colors.grid(column=1, row=0, sticky=W, **paddings)

cor_escolhida_preenchimento = StringVar(root) 
menu_colors_preenchimento = ttk.OptionMenu(
    frame, cor_escolhida_preenchimento,
    'Preto',
    'Preto',
    'Branco',
    'Amarelo',
    'Azul',
    'Verde',
    'Vermelho',
    'Rosa'
)
menu_colors_preenchimento.grid(column=0, row=0, sticky=W, **paddings)


# Área de desenho
canvas = Canvas(frame, bg='white', width=1000, height=1000)
canvas.grid(column=0, row=1, columnspan=2, sticky=W, **paddings)

frame.pack()

# Eventos de mouse associados ao canvas - com seus callbacks
canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)

root.mainloop()