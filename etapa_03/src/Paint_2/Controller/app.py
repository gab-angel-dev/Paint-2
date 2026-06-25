from etapa_03.src.Paint_2.Model.Linha import Linha
from etapa_03.src.Paint_2.Model.LinhaLivre import LinhaLivre
from etapa_03.src.Paint_2.Model.Oval import Oval
from etapa_03.src.Paint_2.Model.Circulo import Circulo
from etapa_03.src.Paint_2.Model.Retangulo import Retangulo
from etapa_03.src.Paint_2.Model.Poligono import Poligono
from etapa_02.interface.janela import App

figuras_classes = {
    "Linha": Linha,
    "Rabisco": LinhaLivre,
    "Retângulo": Retangulo,
    "Oval": Oval,
    "Círculo": Circulo,
    "Poligono": Poligono
}

cores = {
    "Preto": 'black',
    "Branco": 'white',
    "Amarelo": 'yellow',
    "Azul": 'blue',
    "Verde": 'green',
    "Vermelho": 'red',
    "Rosa": 'pink',
    "Cinza": 'gray'
}

root = App(nome='Paint 2')
canvas = root.canvas

instancia_atual = None
historico_figuras = list()


# função para sempre aplicar a figura
def aplicar_figura(*args):
    global instancia_atual
    global historico_figuras
    global cores

    canvas.unbind('<ButtonPress-1>')
    canvas.unbind('<B1-Motion>')
    canvas.unbind('<ButtonRelease-1>')

    cor_borda_aux = root.cor_borda.get()
    if cor_borda_aux in cores:
        cor_borda = cores[cor_borda_aux]
    else:
        cor_borda = 'black'


    cor_pree_aux = root.cor_preenchimento.get()
    if cor_pree_aux in cores:
        cor_preenchimento = cores[cor_pree_aux]
    else:
        cor_preenchimento = 'white'


    tipo_de_figura = root.tipo_figura.get()
    if tipo_de_figura in figuras_classes:
        figura = figuras_classes[tipo_de_figura]

        instancia_atual = figura(
            canvas=canvas,
            historico_figuras=historico_figuras,
            cor_borda=cor_borda,
            cor_preenchimento=cor_preenchimento,
            lados=root.lados.get()
        )
        

        canvas.bind('<ButtonPress-1>', instancia_atual.iniciar_figura)
        canvas.bind('<B1-Motion>', instancia_atual.atualizar_figura)
        canvas.bind('<ButtonRelease-1>', instancia_atual.incluir_figura)

root.tipo_figura.trace('w', aplicar_figura)
root.cor_borda.trace('w', aplicar_figura)
root.cor_preenchimento.trace('w', aplicar_figura)
root.lados.trace('w', aplicar_figura)

root.mainloop()