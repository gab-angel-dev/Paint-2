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
    def incompleta(self):
        pass


