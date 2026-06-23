from abc import ABC, abstractmethod

class Figuras(ABC):
    def __init__(
        self,
        nome: str,
        x1: int, 
        y1: int,
        x2: int,
        y2: int,
        cor_borda: str | None = 'black',
        cor_preenchimento: str | None = 'white',


    
    ):
        super().__init__()
        self.nome = nome
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento


    @abstractmethod
    def iniciar_figura(self):
        pass

    @abstractmethod 
    def atualizar_figura(self):
        pass

    @abstractmethod
    def incluir_figura(self):
        pass

    @abstractmethod
    def desenhar_figura(self):
        pass

    @abstractmethod
    def desenhar_figura_nova(self):
        pass

    @abstractmethod
    def incompleta(self):
        pass


