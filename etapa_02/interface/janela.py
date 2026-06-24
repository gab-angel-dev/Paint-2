import tkinter as tk
from tkinter import ttk, font

class App(tk.Tk):
    def __init__(
            self,
            nome: str = 'Sem Título - Paint 2',
    ):
        
        super().__init__()
        self.nome = nome
        # Titulo , tamanho e cor da tela
        self.title(self.nome)
        self.geometry("1920x1080")
        self.configure(bg='gray20')
        
        # Configuração da estrutura da tela
        self.grid_rowconfigure(index=1 ,weight=1)
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



        # Funções que constroem a tela
        self.construir_barra_menu()




    def construir_barra_menu(self):
        # boato de escolher figura
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

        # botao de escolher cor de borda
        self.cor_borda = tk.StringVar(self.barra_superior, value='Cor da Borda')

        self.menu_cor_borda = tk.OptionMenu(
            self.barra_superior,
            self.cor_borda,
                'Preto',
                'Branco',
                'Amarelo',
                'Azul',
                'Verde',
                'Vermelho',
                'Rosa',
                'Cinza'
        )

        self.menu_cor_borda.config(
            bg='gray20',
            fg='white',
            activebackground="gray30",
            activeforeground="white",
            relief="flat", 
            bd=0,           
            highlightthickness=0
        )

        self.menu_cor_borda.pack(side='left')

        # botao de escolher cor de preenchimento
        self.cor_preenchimento = tk.StringVar(self.barra_superior, value='Cor Preenchimento')

        self.menu_cor_preenchimento = tk.OptionMenu(
            self.barra_superior,
            self.cor_preenchimento,
                'Preto',
                'Branco',
                'Amarelo',
                'Azul',
                'Verde',
                'Vermelho',
                'Rosa',
                'Cinza'
        )

        self.menu_cor_preenchimento.config(
            bg='gray20',
            fg='white',
            activebackground="gray30",
            activeforeground="white",
            relief="flat", 
            bd=0,           
            highlightthickness=0
        )

        self.menu_cor_preenchimento.pack(side='left')

        # botao de ferramenta
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


        # botao deescolher lados do poligono
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


    





if __name__ == "__main__":


    janela = App()
    janela.mainloop()