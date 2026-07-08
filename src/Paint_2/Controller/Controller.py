from tkinter import filedialog

from src.Paint_2.View.View import App
from src.Paint_2.Model.Model import Model


class Controller:
    """
    Controlador da aplicação.

    Atua como intermediário entre a interface gráfica (View) e o
    modelo de dados (Model). É responsável por tratar os eventos
    gerados pelo usuário, criar e atualizar figuras, e solicitar 
    a utilização da interface.
    
    atributos:
        figuras(dict): dicionário que mapeia os nomes das figuras às suas respectivas classes
        model(Model): instância do modelo de dados da aplicação
        view(App): instância da interface gráfica principal
        cor_borda(str): cor da borda atualmente selecionada na interface
        cor_preenchimento(str): cor de preenchimento atualmente selecionada na interface
        nome_figura_atual(str): nome do tipo de figura selecionado (ex: "poligono")
        lados(int): número de lados selecionado para as figuras aplicáveis
        figura_atual(Figuras): instância da figura geométrica que está sendo manipulada
    @author Angel
    @version 1.0
    """
    def __init__(
        self,
        figuras: dict
    ):
        """
        Inicializa o controlador configurando o modelo, a interface e os eventos.
        
        Vincula os eventos de clique, arrasto e soltura do mouse no Canvas,
        configura os comandos dos botões de arquivo e define os rastreadores (traces)
        para capturar mudanças nas opções da interface em tempo real.
                
        @param figuras dicionário contendo as classes das figuras geométricas disponíveis
        """
        self.figuras = figuras
        self.model = Model()      
        self.view = App()

        self.cor_borda = self.view.cor_borda.get()
        self.cor_preenchimento = self.view.cor_preenchimento.get()
        self.nome_figura_atual = self.view.tipo_figura.get()
        self.lados = self.view.lados.get()
        self.figura_atual = None

        self.pegar_figura_atual()

        # Vinculação de eventos do Canvas
        self.view.canvas.bind('<ButtonPress-1>', self.iniciar)
        self.view.canvas.bind('<B1-Motion>', self.atualizar)
        self.view.canvas.bind('<ButtonRelease-1>', self.incluir)

        # Configuração dos botões de Persistência
        self.view.botao_salvar.config(command=self.salvar)
        self.view.botao_abrir.config(command=self.abrir)

        # Rastreadores de estado da interface
        self.view.tipo_figura.trace('w', self.aplicar_figura)
        self.view.cor_borda.trace('w', self.aplicar_figura)
        self.view.cor_preenchimento.trace('w', self.aplicar_figura)
        self.view.lados.trace('w', self.aplicar_figura)

        self.view.mainloop()


    def iniciar(self, event):
        """
        Interpola o evento de clique do mouse para definir o início de uma nova figura.
        
        @param event evento de clique do mouse (tkinter.Event) enviado pelo Canvas
        """
        if self.figura_atual:
            self.figura_atual.iniciar_figura(event) 
    
    def atualizar(self, event):
        """
        Trata o arrasto do mouse, atualizando a figura corrente e redesenhando a tela.
        
        Garante que o histórico anterior e o rascunho em tempo real da figura atual
        sejam renderizados simultaneamente no Canvas.
        
        @param event evento de movimento do mouse (tkinter.Event) com o botão pressionado
        """
        if self.figura_atual:
            self.figura_atual.atualizar_figura(event)
            figuras = self.model.get_figuras()
            self.view.redesenhar(figuras, self.figura_atual.figura_nova)
    
    def incluir(self, event):
        """
        Finaliza o desenho da figura ao soltar o clique do mouse.
        
        Valida se a figura criada possui dimensões válidas e, se correto, 
        solicita ao modelo a sua inclusão definitiva no histórico, limpando o Canvas.
        
        @param event evento de soltura do botão do mouse (tkinter.Event)
        """
        if self.figura_atual:
            if not self.figura_atual.incompleta(self.figura_atual.figura_nova):
                self.model.adicionar_figura(self.figura_atual.figura_nova)
            self.view.redesenhar(self.model.get_figuras())

    def salvar(self):
        """
        Abre uma caixa de diálogo para salvar o projeto atual em um arquivo do sistema.
        
        Caso o usuário selecione um caminho válido, delega ao modelo a gravação 
        dos dados das figuras no formato binário `.paint`.
        """
        caminho = filedialog.asksaveasfilename(
            defaultextension=".paint",
            filetypes=[("Arquivo Paint", "*.paint")]
        )
        if caminho:
            self.model.salvar_arquivo(caminho)

    def abrir(self):
        """
        Abre uma caixa de diálogo para carregar um projeto salvo anteriormente.
        
        Caso um arquivo válido `.paint` seja selecionado, atualiza o modelo 
        com os dados recuperados e força a atualização completa do Canvas da View.
        """
        caminho = filedialog.askopenfilename(
            defaultextension=".paint",
            filetypes=[("Arquivo Paint", "*.paint")]
        )
        if caminho:
            self.model.abrir_arquivo(caminho)
            self.view.redesenhar(self.model.get_figuras())

    def pegar_figura_atual(self):
        """
        Instancia a classe correspondente ao tipo de figura selecionado na interface gráfica.
        
        Cria o objeto passando os atributos de cores e lados atualmente vigentes 
        para que a figura esteja pronta para receber as coordenadas de desenho.
        """
        if self.nome_figura_atual in self.figuras:
            self.figura_atual = self.figuras[self.nome_figura_atual](
                cor_borda=self.cor_borda,
                cor_preenchimento=self.cor_preenchimento,
                lados=self.lados
            )

    def aplicar_figura(self, *args):
        """
        Atualiza as propriedades do controlador com base nos seletores da View.
        
        Método de retorno de chamada (callback) acionado sempre que há alteração de 
        cores, tipo de forma ou número de lados na interface do usuário.
        
        @param args argumentos dinâmicos enviados automaticamente pelo rastreador de variáveis (trace)
        """
        self.cor_borda = self.view.cor_borda.get()
        self.cor_preenchimento = self.view.cor_preenchimento.get()
        self.nome_figura_atual = self.view.tipo_figura.get()
        self.lados = self.view.lados.get()
        
        self.pegar_figura_atual()