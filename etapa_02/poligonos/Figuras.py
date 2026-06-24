from abc import ABC, abstractmethod

class Figuras(ABC):
    def __init__(
        self,
        canvas,
        historico_figuras: list[tuple] = [],
        x1: int = 0, 
        y1: int = 0,
        x2: int = 0,
        y2: int = 0,
        nome: str | None = None,
        cor_borda: str | None = 'black',
        cor_preenchimento: str | None = 'white',
        lados: int = 3
    
    ):
        super().__init__()
        self.nome = nome
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento
        self.canvas = canvas
        self.historico_figuras = historico_figuras
        self.lados = lados


    @abstractmethod
    def iniciar_figura(self, event):
        pass

    @abstractmethod 
    def atualizar_figura(self, event):
        pass

    @abstractmethod
    def incluir_figura(self):
        pass

    @abstractmethod
    def desenhar_figura(self):
        self.canvas.delete("all")
        for fig, values, cor_outline, cor_fill in self.historico_figuras:
            if fig == "linha":
                self.canvas.create_line(values[0], values[1], values[2], values[3])
            elif fig == "rabisco":
                self.canvas.create_line(values)
            elif fig == 'retangulo':
                self.canvas.create_rectangle(values, outline=cor_outline, fill=cor_fill ,width=2)
            elif fig == 'oval':
                self.canvas.create_oval(values, outline=cor_outline, fill=cor_fill, width=2)
            elif fig == 'circulo':
                self.canvas.create_oval(values, outline=cor_outline, fill=cor_fill, width=2)
            else:
                self.canvas.create_polygon(values, outline=cor_outline, fill=cor_fill, dash=(4, 2), width=2)


    @abstractmethod
    def desenhar_figura_nova(self):
        pass

    @abstractmethod
    def incompleta(self):
        pass


