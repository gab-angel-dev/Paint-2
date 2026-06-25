from etapa_03.src.Paint_2.View.View import App
from etapa_03.src.Paint_2.Model.Model import Model
from etapa_03.src.Paint_2.Model.Figuras import Figuras


class Controller:
    def __init__(self, figura: Figuras):
        self.figura_atual = figura
        self.model = Model()      
        self.view = App() 


        self.view.tipo_figura.trace('w', self.aplicar_figura)
        self.view.cor_borda.trace('w', self.aplicar_figura)
        self.view.cor_preenchimento.trace('w', self.aplicar_figura)
        self.view.lados.trace('w', self.aplicar_figura)

        self.view.canvas.bind('<ButtonPress-1>', self.iniciar)
        self.view.canvas.bind('<B1-Motion>', self.atualizar)
        self.view.canvas.bind('<ButtonRelease-1>', self.incluir)
    

        self.view.mainloop()

    
    # fazer a lógica de conseguir acessar as figuras

    def iniciar(self, event):
        self.figura_atual.iniciar_figura(event) 
        # esse figura_atual é um atributo das Classes de figuras
    
    def atualizar(self, event):
        self.figura_atual.atualizar_figura(event)
        figuras = self.model.get_figuras()
        self.view.redesenhar(figuras, self.figura_atual.figura_nova)
    
    def incluir(self, event):
        if not self.figura_atual.incompleta(self.figura_atual.figura_nova):
            self.model.adicionar_figura(self.figura_atual.figura_nova)
        self.view.redesenhar(self.model.get_figuras())