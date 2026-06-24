from etapa_02.poligonos.Linha import Linha
from etapa_02.poligonos.LinhaLivre import LinhaLivre
from etapa_02.poligonos.Oval import Oval
from etapa_02.poligonos.Circulo import Circulo
from etapa_02.poligonos.Retangulo import Retangulo
from etapa_02.poligonos.Poligono import Poligono
from etapa_02.interface.janela import App

figuras_classes = {
    "Linha": Linha,
    "Rabisco": LinhaLivre,
    "Retângulo": Retangulo,
    "Oval": Oval,
    "Círculo": Circulo,
    "Poligono": Poligono
}

root = App(nome='Paint 2')
canvas = root.canvas

instancia_atual = None
historico_figuras = []


# função para sempre aplicar a figura
def aplicar_figura(*args):
    global instancia_atual
    global historico_figuras

    canvas.unbind('<ButtonPress-1>')
    canvas.unbind('<B1-Motion>')
    canvas.unbind('<ButtonRelease-1>')

    tipo_de_figura = root.tipo_figura.get()

    if tipo_de_figura in figuras_classes:
        figura = figuras_classes[tipo_de_figura]
        instancia_atual = figura(
            canvas=canvas,
            historico_figuras=historico_figuras,
        )
        

        canvas.bind('<ButtonPress-1>', instancia_atual.iniciar_figura)
        canvas.bind('<B1-Motion>', instancia_atual.atualizar_figura)
        canvas.bind('<ButtonRelease-1>', instancia_atual.incluir_figura)

root.tipo_figura.trace('w', aplicar_figura)

root.mainloop()