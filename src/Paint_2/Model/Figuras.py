from abc import ABC, abstractmethod

class Figuras(ABC):
    """
    Classe abstrata que representa uma figura geométrica genérica.

    Responsabilidade: servir como base para todas as formas geométricas do 
    sistema, definindo os atributos comuns (cores e lados) e a interface 
    obrigatória para a criação e atualização de figuras na tela.
            
    atributos:
        cor_borda(str): cor da borda da figura
        cor_preenchimento(str): cor de preenchimento da figura
        lados(int): número de lados da figura (se aplicável)
        figura_nova(tuple): tupla contendo os dados de renderização da figura
    @author Jorge
    @version 1.0
    """
    def __init__(
        self,
        cor_borda: str = 'black',
        cor_preenchimento: str = 'white',
        lados: int = 3
    ):
        """
        Inicializa as propriedades básicas de uma figura geométrica.
                
        @param cor_borda cor da borda da figura (padrão: "black")
        @param cor_preenchimento cor de preenchimento da figura (padrão: "white")
        @param lados número de lados da figura (padrão: 3)
        """
        self._cor_borda = cor_borda
        self._cor_preenchimento = cor_preenchimento
        self._lados = lados
        self._figura_nova = None


    # Tornar os atributos read-only, somente para leitura não permitindo que seja modficado durante o código aumentando a segurança

    @property
    def cor_borda(self):
        return self._cor_borda
    
    @property
    def cor_preenchimento(self):
        return self._cor_preenchimento

    @property
    def lados(self):
        return self._lados
    

    @abstractmethod
    def iniciar_figura(self, event):
        """
        Define o ponto inicial do desenho da figura a partir do clique do mouse.
        
        Método abstrato que deve ser implementado pelas classes filhas para 
        capturar as coordenadas iniciais do desenho.
                
        @param event evento de clique do mouse (tkinter.Event) contendo 
        as coordenadas x e y iniciais
        """
        pass

    @abstractmethod
    def atualizar_figura(self, event):
        """
        Atualiza o tamanho e o estado da figura conforme o mouse é arrastado.
        
        Método abstrato que deve ser implementado pelas classes filhas para 
        recalcular as dimensões da figura em tempo real.
                
        @param event evento de movimento do mouse (tkinter.Event) contendo 
        a posição atual do cursor
        """
        pass

    @abstractmethod
    def incompleta(self, figura):
        """
        Verifica se a figura possui dimensões válidas para ser registrada.
        
        Método abstrato que deve ser implementado pelas classes filhas para 
        evitar o registro de figuras sem tamanho (cliques simples sem arrastar).
                
        @param figura tupla contendo os dados da figura a ser validada
        @return True se a figura for inválida/incompleta; False caso contrário
        """
        pass