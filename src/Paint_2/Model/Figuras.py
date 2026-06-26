from abc import ABC, abstractmethod

class Figuras(ABC):
    def __init__(
        self,
        cor_borda: str = 'black',
        cor_preenchimento: str = 'white',
        lados: int = 3
    ):
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento
        self.lados = lados
        self.figura_nova = None

    @abstractmethod
    def iniciar_figura(self, event):
        pass

    @abstractmethod
    def atualizar_figura(self, event):
        pass

    @abstractmethod
    def incompleta(self, figura):
        pass