from tkinter import filedialog

from src.Paint_2.View.View import App
from src.Paint_2.Model.Model import Model


class Controller:
    """
    Controlador da aplicação.

    Atua como intermediário entre a interface gráfica (View) e o
    modelo de dados (Model). É responsável por tratar os eventos
    gerados pelo usuário, criar e atualizar figuras, e solicitar 
    a utilizaçao da interface.
    """
    def __init__(
        self,
        figuras: dict
    ):

        self.figuras = figuras
        self.model = Model()      
        self.view = App()

        self.cor_borda = self.view.cor_borda.get()
        self.cor_preenchimento = self.view.cor_preenchimento.get()
        self.nome_figura_atual = self.view.tipo_figura.get()
        self.lados = self.view.lados.get()
        self.figura_atual = None

        self.pegar_figura_atual()

        self.view.canvas.bind('<ButtonPress-1>', self.iniciar)
        self.view.canvas.bind('<B1-Motion>', self.atualizar)
        self.view.canvas.bind('<ButtonRelease-1>', self.incluir)

        self.view.botao_salvar.config(command=self.salvar)
        self.view.botao_abrir.config(command=self.abrir)

        self.view.tipo_figura.trace('w', self.aplicar_figura)
        self.view.cor_borda.trace('w', self.aplicar_figura)
        self.view.cor_preenchimento.trace('w', self.aplicar_figura)
        self.view.lados.trace('w', self.aplicar_figura)

        self.view.mainloop()


    def iniciar(self, event):
        if self.figura_atual:
            self.figura_atual.iniciar_figura(event) 
    
    def atualizar(self, event):
        if self.figura_atual:
            self.figura_atual.atualizar_figura(event)
            figuras = self.model.get_figuras()
            self.view.redesenhar(figuras, self.figura_atual.figura_nova)
    
    def incluir(self, event):
        if self.figura_atual:
            if not self.figura_atual.incompleta(self.figura_atual.figura_nova):
                self.model.adicionar_figura(self.figura_atual.figura_nova)
            self.view.redesenhar(self.model.get_figuras())

    def salvar(self):
        caminho = filedialog.asksaveasfilename(
            defaultextension=".paint",
            filetypes=[("Arquivo Paint", "*.paint")]
        )
        if caminho:
            self.model.salvar_arquivo(caminho)

    def abrir(self):
        caminho = filedialog.askopenfilename(
            defaultextension=".paint",
            filetypes=[("Arquivo Paint", "*.paint")]
        )
        if caminho:
            self.model.abrir_arquivo(caminho)
            self.view.redesenhar(self.model.get_figuras())

    def pegar_figura_atual(self):
        if self.nome_figura_atual in self.figuras:
            self.figura_atual = self.figuras[self.nome_figura_atual](
                cor_borda=self.cor_borda,
                cor_preenchimento=self.cor_preenchimento,
                lados=self.lados
            )

    def aplicar_figura(self, *args):
        self.cor_borda = self.view.cor_borda.get()
        self.cor_preenchimento = self.view.cor_preenchimento.get()
        self.nome_figura_atual = self.view.tipo_figura.get()
        self.lados = self.view.lados.get()
        
        self.pegar_figura_atual()