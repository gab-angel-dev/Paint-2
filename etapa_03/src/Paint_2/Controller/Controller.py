from etapa_03.src.Paint_2.View.View import App
from etapa_03.src.Paint_2.Model.Model import Model



class Controller:
    def __init__(
        self,
        figuras: dict,
        cores: dict
    ):

        self.figuras = figuras
        self.cores = cores
        self.model = Model()      
        self.view = App()


        self.cor_borda = self.view.cor_borda.get()
        self.cor_preenchimento = self.view.cor_preenchimento.get()
        self.figura_atual = self.view.tipo_figura.get()
        self.lados = self.view.lados.get()


        self.pegar_cor()
        self.pegar_figura_atual()


        self.view.canvas.bind('<ButtonPress-1>', self.iniciar)
        self.view.canvas.bind('<B1-Motion>', self.atualizar)
        self.view.canvas.bind('<ButtonRelease-1>', self.incluir)


        self.view.tipo_figura.trace('w', self.aplicar_figura)
        self.view.cor_borda.trace('w', self.aplicar_figura)
        self.view.cor_preenchimento.trace('w', self.aplicar_figura)
        self.view.lados.trace('w', self.aplicar_figura)

    
        self.view.mainloop()


    def iniciar(self, event):
        self.figura_atual.iniciar_figura(event) 
    
    def atualizar(self, event):
        self.figura_atual.atualizar_figura(event)
        figuras = self.model.get_figuras()
        self.view.redesenhar(figuras, self.figura_atual.figura_nova)
    
    def incluir(self, event):
        if not self.figura_atual.incompleta(self.figura_atual.figura_nova):
            self.model.adicionar_figura(self.figura_atual.figura_nova)
        self.view.redesenhar(self.model.get_figuras())


    def pegar_cor(self):
        # pega cor da borda
        if self.cor_borda in self.cores:
            self.cor_borda = self.cores[self.cor_borda]
        else:
            self.cor_borda = 'black'

        # pega cor do preenchimento
        if self.cor_preenchimento in self.cores:
            self.cor_preenchimento = self.cores[self.cor_preenchimento]
        else:
            self.cor_preenchimento = 'white'

    # instanciao objeto da Figura correspondente
    def pegar_figura_atual(self):
        if self.figura_atual in self.figuras:
            self.figura_atual = self.figuras[self.figura_atual](
                cor_borda = self.cor_borda,
                cor_preenchimento = self.cor_preenchimento,
                lados = self.lados
            )
    
    def aplicar_figura(self, *args):
        self.cor_borda = self.view.cor_borda.get()
        self.cor_preenchimento = self.view.cor_preenchimento.get()
        self.figura_atual = self.view.tipo_figura.get()
        self.lados = self.view.lados.get()
        
        self.pegar_cor()
        self.pegar_figura_atual()