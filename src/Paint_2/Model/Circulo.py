from src.Paint_2.Model.Figuras import Figuras



class Circulo(Figuras):
    """
    Representar um circulo desenhado na tela.

    Esta classe herda de ``Figuras`` e é responsável por armazenar
    as informações necessárias para criar e atualizar uma figura
    durante o desenho realizado pelo usuário.


    atributos:
        raio(int): raio atual do circulo
        cor_borda(str): cor da borda
        cor_preenchimento(str): cor de preenchiemnto
        lados(int): números de lados (mantidos por compatibilidade com a superclasse)

    """
    def __init__(
        self,
        cor_borda: str = 'black',
        cor_preenchimento: str = 'white',
        lados = 3
        ):
        super().__init__(
            cor_borda,
            cor_preenchimento,
            lados
            )
        
        self.raio = 0 


    def iniciar_figura(self, event):
        """
        define o ponto inicial da figura.
        """
        self.inic_x = event.x
        self.inic_y = event.y

    def atualizar_figura(self, event):
        """
        atualiza as dimenções da figura conforme o monvimento do mouse.
        """
        self.raio = min(
        abs(event.x-self.inic_x),
        abs(event.y-self.inic_y)
        )
        self.figura_nova = (
            'circulo', 
            (self.inic_x, self.inic_y, self.inic_x +self.raio, self.inic_y +self.raio),
            self.cor_borda,
            self.cor_preenchimento
            )

      
    def incompleta(self, event):
        """
        retorna True para quando o tamanho da figura não for válido.
        """
        values = self.figura_nova[1]
        return (values[0], values[1]) == (values[2], values[3])
    