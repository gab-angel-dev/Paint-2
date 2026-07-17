import tkinter as tk
from tkinter import colorchooser

class App(tk.Tk):
    """
    Interface gráfica principal da aplicação (View).

    Responsabilidade: construir a janela do programa, gerenciar os elementos
    visuais (Canvas, botões, menus) e renderizar as figuras geométricas
    na tela de acordo com os dados fornecidos pelo modelo.
            
    atributos:
        nome(str): título da janela da aplicação
        barra_superior(tk.Frame): contêiner superior para os botões de controle
        canvas(tk.Canvas): área de desenho onde as figuras são renderizadas
        tipo_figura(tk.StringVar): variável que armazena o tipo de forma selecionado
        cor_borda(tk.StringVar): variável que armazena a cor de borda atual
        cor_preenchimento(tk.StringVar): variável que armazena a cor de preenchimento atual
        ferramenta(tk.StringVar): variável que armazena a ferramenta secundária (ex: Borracha)
        lados(tk.IntVar): variável que armazena a quantidade de lados para polígonos
    @author Angel
    @version 1.0
    """
    def __init__(
            self,
            nome: str = 'Sem Título - Paint 2',
    ):
        """
        Inicializa a janela principal do sistema, configurando layout e componentes.
        
        Define as dimensões da aplicação, a estrutura de grid (linhas e colunas),
        cria os frames principais (barra de ferramentas e canvas) e invoca a 
        construção dos componentes do menu.
                
        @param nome título padrão exibido na barra superior do sistema (padrão: "Sem Título - Paint 2")
        """
        super().__init__()
        self.nome = nome
        self.title(self.nome)
        self.geometry("1920x1080")
        self.configure(bg='gray20')
        
        # Configuração da estrutura da tela
        self.grid_rowconfigure(index=1, weight=1)
        self.grid_columnconfigure(index=0, weight=1)

        # Barra superior onde tem os botões e as funcionalidades
        self.barra_superior = tk.Frame(
            self,
            background='gray20',
            height=25,
            width=1920
        )
        self.barra_superior.grid(row=0, column=0, sticky='ew')

        # Canvas
        self.canvas = tk.Canvas(
            self,
            background='white',
            height=1000,
            width=1920,
        )
        self.canvas.grid(row=1, column=0, sticky='nsew', padx=(100, 20), pady=1)

        # Função que constrói a tela
        self.construir_barra_menu()


    def construir_barra_menu(self):
        """
        Instancia, estiliza e posiciona todos os componentes da barra de ferramentas superior.
        
        Configura os menus suspensos (OptionMenu) para formas e ferramentas, os botões
        de seleção de cor, o seletor numérico (Spinbox) de lados e os botões de arquivo.
        """
        # Botão de escolher figura
        self.tipo_figura = tk.StringVar(self.barra_superior, value="Formas")
        
        self.menu_figura = tk.OptionMenu(
            self.barra_superior,
            self.tipo_figura,
                "Linha",
                "Rabisco",
                "Retângulo",
                "Oval",
                "Círculo",
                "Poligono"
        )

        self.menu_figura.config(
            bg='gray20',
            fg='white',
            activebackground="gray30",
            activeforeground="white",
            relief="flat", 
            bd=0,           
            highlightthickness=0
        )

        self.menu_figura.pack(side='left')

        # Botão de escolher cor de borda
        self.cor_borda = tk.StringVar(self.barra_superior, value='black')

        self.botao_cor_borda = tk.Button(
            self.barra_superior,
            text='Cor da Borda',
            command=self.escolher_cor_borda
        )

        self.botao_cor_borda.config(
            bg='gray20',
            fg='white',
            activebackground="gray30",
            activeforeground="white",
            relief="flat", 
            bd=0,           
            highlightthickness=0
        )

        self.botao_cor_borda.pack(side='left')

        # Botão de escolher cor de preenchimento
        self.cor_preenchimento = tk.StringVar(self.barra_superior, value='white')

        self.botao_cor_preenchimento = tk.Button(
            self.barra_superior,
            text='Cor Preenchimento',
            command=self.escolher_cor_preenchimento
        )

        self.botao_cor_preenchimento.config(
            bg='gray20',
            fg='white',
            activebackground="gray30",
            activeforeground="white",
            relief="flat", 
            bd=0,           
            highlightthickness=0
        )

        self.botao_cor_preenchimento.pack(side='left')

        # Botão de remover preenchimento (deixar vazio/transparente)
        self.botao_sem_preenchimento = tk.Button(
            self.barra_superior,
            text='Sem Preenchimento',
            command=self.remover_preenchimento
        )

        self.botao_sem_preenchimento.config(
            bg='gray20',
            fg='white',
            activebackground="gray30",
            activeforeground="white",
            relief="flat", 
            bd=0,           
            highlightthickness=0
        )

        self.botao_sem_preenchimento.pack(side='left')

        # Botão de ferramenta
        self.ferramenta = tk.StringVar(self.barra_superior, value='Ferramenta')

        self.menu_ferramenta = tk.OptionMenu(
            self.barra_superior,
            self.ferramenta,
               "Borracha"
        )

        self.menu_ferramenta.config(
            bg='gray20',
            fg='white',
            activebackground="gray30",
            activeforeground="white",
            relief="flat", 
            bd=0,           
            highlightthickness=0
        )

        self.menu_ferramenta.pack(side='left')

        # Botão de escolher lados do polígono
        self.lados = tk.IntVar(self.barra_superior, value=3)

        self.spinbox_lados = tk.Spinbox(
            self.barra_superior,
            from_=3,
            to=20,
            textvariable=self.lados,
            width=3,
            bg='gray20',
            fg='white',
            buttonbackground='gray20',
            relief='flat',
        )

        self.spinbox_lados.pack(side='left')

        # Botão de salvar arquivo
        self.botao_salvar = tk.Button(
            self.barra_superior,
            text='Salvar'
        )

        self.botao_salvar.config(
            bg='gray20',
            fg='white',
            activebackground="gray30",
            activeforeground="white",
            relief="flat", 
            bd=0,           
            highlightthickness=0
        )

        self.botao_salvar.pack(side='right')

        # Botão de abrir arquivo
        self.botao_abrir = tk.Button(
            self.barra_superior,
            text='Abrir'
        )

        self.botao_abrir.config(
            bg='gray20',
            fg='white',
            activebackground="gray30",
            activeforeground="white",
            relief="flat", 
            bd=0,           
            highlightthickness=0
        )

        self.botao_abrir.pack(side='right')


    def escolher_cor_borda(self):
        """
        Exibe um seletor gráfico de cores para definir a cor da borda das figuras.
        
        Se uma cor válida for escolhida, atualiza a variável correspondente e altera 
        o fundo do botão para fornecer feedback visual ao usuário.
        """
        cor = colorchooser.askcolor(title="Escolha a cor da borda")
        if cor[1]:
            self.cor_borda.set(cor[1])
            self.botao_cor_borda.config(bg=cor[1])

    def escolher_cor_preenchimento(self):
        """
        Exibe um seletor gráfico de cores para definir o preenchimento das figuras.
        
        Se uma cor válida for escolhida, atualiza a variável correspondente e altera 
        o fundo do botão para fornecer feedback visual ao usuário.
        """
        cor = colorchooser.askcolor(title="Escolha a cor de preenchimento")
        if cor[1]:
            self.cor_preenchimento.set(cor[1])
            self.botao_cor_preenchimento.config(bg=cor[1])

    def remover_preenchimento(self):
        self.cor_preenchimento.set("")
        self.botao_cor_preenchimento.config(bg="gray20")
    
    def redesenhar(self, figuras, figura_nova = None):
        """
        Limpa a tela e renderiza todo o histórico de figuras e o rascunho atual.
        
        Este método reconstrói o Canvas do zero a cada atualização. Ele itera sobre 
        a lista de figuras consolidadas e, opcionalmente, desenha a figura provisória 
        que está sendo arrastada em tempo real.
                
        @param figuras lista de tuplas contendo todas as figuras salvas no histórico do modelo
        @param figura_nova tupla que representa o estado atual da figura em desenho (opcional)
        """
        self.canvas.delete("all")

        for fig, values, cor_outline, cor_fill in figuras:
            if fig == "linha":
                self.canvas.create_line(values[0], values[1], values[2], values[3], fill=cor_outline, width=2)
            elif fig == "rabisco":
                self.canvas.create_line(values, fill=cor_outline, width=2)
            elif fig == 'retangulo':
                self.canvas.create_rectangle(values, outline=cor_outline, fill=cor_fill, width=2)
            elif fig == 'oval':
                self.canvas.create_oval(values, outline=cor_outline, fill=cor_fill, width=2)
            elif fig == 'circulo':
                self.canvas.create_oval(values, outline=cor_outline, fill=cor_fill, width=2)
            else:
                self.canvas.create_polygon(values, outline=cor_outline, fill=cor_fill, dash=(4, 2), width=2)
        
        if figura_nova:
            fig, values, cor_outline, cor_fill = figura_nova
            if fig == "linha":
                self.canvas.create_line(values[0], values[1], values[2], values[3], fill=cor_outline, width=2)
            elif fig == "rabisco":
                self.canvas.create_line(values, fill=cor_outline, width=2)
            elif fig == 'retangulo':
                self.canvas.create_rectangle(values, outline=cor_outline, fill=cor_fill, width=2)
            elif fig == 'oval':
                self.canvas.create_oval(values, outline=cor_outline, fill=cor_fill, width=2)
            elif fig == 'circulo':
                self.canvas.create_oval(values, outline=cor_outline, fill=cor_fill, width=2)
            else:
                self.canvas.create_polygon(values, outline=cor_outline, fill=cor_fill, dash=(4, 2), width=2)