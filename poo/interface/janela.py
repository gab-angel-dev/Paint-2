import tkinter as ttk


class App(ttk.Tk):
    def __init__(self):
        super().__init__()

    
        self.title('Meu App')
        self.geometry('900x600')

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)


    
        self.barra_lateral = ttk.Frame(self, width=200)
        self.barra_lateral.grid(row=0, column=0, sticky='nsew')

        


janela = App()
janela.mainloop()