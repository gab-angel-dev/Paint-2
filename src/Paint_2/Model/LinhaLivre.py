from src.Paint_2.Model.Figuras import Figuras

class LinhaLivre(Figuras):
    """
    Representar um rabisco desenhado na tela.
    
    Esta classe herda de ``Figuras`` e é responsável por armazenar
    as informações necessárias para criar e atualizar uma figura
    durante o desenho realizado pelo usuário.
    
    
    atributos:
        cor_borda(str): cor da borda
        cor_preenchimento(str): cor de preenchiemnto
        lados(int): números de lados (mantidos por compatibilidade com a superclasse)
    """
    def __init__(
        self,
        cor_borda: str = 'black',
        cor_preenchimento: str = 'white',
        lados =3 
        ):
        super().__init__(
            cor_borda,
            cor_preenchimento,
            lados
            )


    def iniciar_figura(self, event):
        """
        define o ponto inicial da figura.
        """
        self.figura_nova  = (
            "rabisco",
            ([(event.x, event.y)]),
            self.cor_borda,
            self.cor_preenchimento
        )

    def atualizar_figura(self, event):
        """
        atualiza as dimenções da figura conforme o monvimento do mouse.
        """
        self.figura_nova[1].append((event.x, event.y))
    
    def incompleta(self, event):
        """
        retorna True para quando o tamanho da figura não for válido.
        """
        return len(self.figura_nova[1]) <=1